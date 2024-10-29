from django.shortcuts import render
from.models import visualdef,formularioenvio

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
    

# Create your views here.
