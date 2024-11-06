from .models import Cartao
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
import base64
import google.generativeai as genai
import os
import PIL.Image

# Create your views here.
def form_webcam(request):
        return render(request, "form_webcam.html")
def ler_img(request):
        context = {}
        if request.method == 'POST':
                img=request.POST.get('imagem')

              

                imgSerializedSplit = base64.b64decode(
                        img.split(',')[1]
                )

                request.FILES['imagem'] = ContentFile(
                        imgSerializedSplit,name='imgSerializedSplit.jpg'
                )

                cartao = Cartao()

                cartao.imagem = request.FILES['imagem']

                cartao.save()

                genai.configure(api_key="AIzaSyCrJHeuVlhGitTdgmnlDY_i7ETfiRMFTC0")

                model = genai.GenerativeModel("gemini-1.5-flash")
                imagemCarreda = PIL.Image.open(cartao.imagem)
                response = model.generate_content(["Gere um texto descrevendo a imagem, para uma pessoa cega: ",imagemCarreda])
                print(response.text),

                mensagem = response.text

                context = {
                "descricao":mensagem,
                "resposta": cartao,
                }

        

        return render(request, "form_webcam.html", context)
def formulario(request):
    return render(request, "formulario.html")

def ler_img(request):

    context = {}

    # Recebe os dados da imagem.
    if request.method == "POST":

        # Deserializando a imagem
        img = request.POST.get('imagem')
        imgSerializedSplited = base64.b64decode(img.split(',')[1])

        # Armazenando a imagem.
        request.FILES["imagem"] = ContentFile(
            imgSerializedSplited, name = 'imgSerializedSplited.jpg')
        
        cartao = Cartao()

        cartao.imagem = request.FILES["imagem"]
        cartao.remetente = ""
        cartao.destinatario = ""
        cartao.mensagem = ""

        cartao.save()
    
        # Código para carregar a imagem no gemini.

    

        # Código para salvar a imagem
        if "imagem" in request.FILES:
            cartao = Cartao()

            cartao.imagem = request.FILES["imagem"]

            cartao.save()

            # Código para enviar a imagem para a IA
            GOOGLE_API_KEY = "AIzaSyDxIxs3w29oz4023U0yilB5_CIZqqGVnOk"

            genai.configure(api_key=GOOGLE_API_KEY)

            model = genai.GenerativeModel("gemini-1.5-flash")
            imagemCarregada = PIL.Image.open(cartao.imagem)
            response = model.generate_content(["Gere um texto descrevendo a imagem para uma pessoa cega: \n", imagemCarregada])
            print(response.text)

            mensagem = response.text

        context = {"imagem": cartao.imagem, "texto": mensagem}

    return redirect("formulario")

    
def descricao(request):
    return render(request, "descricao.html")