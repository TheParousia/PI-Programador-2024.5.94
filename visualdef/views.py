from django.shortcuts import render, redirect

# Create your views here.
from.models import MeuModelo
from .forms import MeuFormulario

# Create your views here.
def formularioenvio(request):
    return render(request,"visualdef.html")

def comando(request):
    comando=request.GET.get("comando")
    

    contexto={
        "comando":comando,
        
    }

    return render(request,"visualdef.HTML", contexto)


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
    
   