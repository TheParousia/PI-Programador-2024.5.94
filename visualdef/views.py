from .models import Cartao
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
import base64
import google.generativeai as genai
import os
import PIL.Image

<<<<<<< HEAD
# Create your views here.
def sobreNos(request):
    return render(request, 'sobre_nos2.html')
=======
from.models import visualdef,formularioenvio
from.models import Meumodelo
from .forms import MeuFormulario

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

def formularioenvio(request):
    return render(request,"formularioenvio")

def formularioenvio(request):
    comando=request.GET.get("comando")
   
    if comando!=None:
        #criação do objeto usando a classe cartão
        visualdef=visualdef()
        #Uso dos dados vindo do front-end
        #para preencher o objeto cartão
        formularioenvio.comando=comando
        
        visualdef.visualdef()

    contexto={
        "comando":comando,
        
    }


    return render(request,"visualdef.html",contexto)
    

def formularioenvio(request):
    return render(request,"visualdef.html")

def comando(request):
    comando=request.GET.get("comando")
    

    contexto={
        "comando":comando,
        
    }

    return render(request,"visualdef.html", contexto)


def upload_imagem(request):
    if request.method == 'POST':
        form = MeuFormulario(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_imagem')
    else:
        form = MeuFormulario()
    return render(request, 'meu_template.html', {'form': form})
def webcam(request):
    return render(request,"webcam.html")
def visualdef(request):
    if request.method == 'POST':
        form = MeuFormulario(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('visualdef_html')
    else:
        form = MeuFormulario()


    return render(request,"visualdef.html")
def ler_img(request):
    context = {}
    if request.method == 'POST':
        img = request.POST.get('imagem')
        imgSerialSplited = base64.b64decode(img.split(",")[1])

        print(imgSerialSplited)

        request.FILES["imagem"] = ContentFile(
            imgSerialSplited,name='imgSerialSplitedSplited.jpg'

        )
        cartao = Meumodelo()


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

        context = {"imagem": cartao.imagem, "descricao": mensagem}

    return render(request, "formulario.html", context)

    
def descricao(request):
    return redirect("webcam")
>>>>>>> main
