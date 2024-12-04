from .models import Meumodelo
from .forms import MeuFormulario
from .models import Cartao
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
import base64
import google.generativeai as genai
import os
import PIL.Image

from .models import Meumodelo


def sobreNos(request):
    return render(request, 'sobre_nos2.html')


def ler_img(request):
    context = {}
    if request.method == 'POST':
        img = request.POST.get('imagem')

        tipodescricao = request.POST.get('tipodescricao')

        prompt = "faça apenas a descrição da imagem,sem responder que sim."

        if tipodescricao == '1':
            prompt = "Faça a descriçao detalhada da imagem capturada."

        elif tipodescricao == '2':
            prompt = "Descreva o valor total das cedulas ou moedas."

        elif tipodescricao == '3':
            prompt = "Faça apenas a descricao das pessoas detalhada."

        imgSerializedSplit = base64.b64decode(
            img.split(',')[1]
        )

        request.FILES['imagem'] = ContentFile(
            imgSerializedSplit, name='imgSerializedSplit.jpg'
        )

        cartao = Cartao()

        cartao.imagem = request.FILES['imagem']

        cartao.save()

        genai.configure(api_key="AIzaSyCrJHeuVlhGitTdgmnlDY_i7ETfiRMFTC0")

        model = genai.GenerativeModel("gemini-1.5-flash")
        imagemCarreda = PIL.Image.open(cartao.imagem)
        response = model.generate_content(
            [prompt, imagemCarreda])
        print(response.text),

        mensagem = response.text

        context = {
            "descricao": mensagem,
        }

    return render(request, "webcam.html", context)


def webcam(request):

    context = {}

    return render(request, "webcam.html", context)


def sobreNos(request):
    return render(request, 'sobre_nos2.html')
