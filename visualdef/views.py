from django.shortcuts import render

# Create your views here.
def sobreNos(request):
    return render(request, 'sobre_nos.html')
