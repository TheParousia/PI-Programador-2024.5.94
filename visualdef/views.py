from django.shortcuts import render

# Create your views here.
from.models import visualdef,formularioenvio
# Create your views here.
def formularioenvio(request):
    return render(request,"visualdef.html")

def comando(request):
    comando=request.GET.get("comando")
    

    contexto={
        "comando":comando,
        
    }

    return render(request,"visualdef.HTML", contexto)
    
   