from django.shortcuts import redirect, render
from django.core.files.base import ContentFile
from.models import Cartao
import google.generativeai as genai
import PIL.Image
import base64
import os

# Create your views here.
def descricao(request):
    return render(request, "descricao.html")

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
    return redirect("formulario")