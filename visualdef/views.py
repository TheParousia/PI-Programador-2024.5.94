import base64
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
from.models import visualdef,formularioenvio

from.models import Meumodelo

from .forms import MeuFormulario

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
    return redirect("webcam")

    
   