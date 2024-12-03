from .models import Meumodelo
from .forms import MeuFormulario
from .models import Cartao
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
import base64
import google.generativeai as genai
import os
import PIL.Image



def ler_img(request):
    context = {}
    if request.method == 'POST':
        img = request.POST.get('imagem')

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
            ["Gere um texto descrevendo a imagem, para uma pessoa cega: ", imagemCarreda])
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
