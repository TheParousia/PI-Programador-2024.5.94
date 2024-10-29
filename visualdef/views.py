from django.shortcuts import render

# Create your views here.
def descricao(request):
        return render(request, "Descricao.html")