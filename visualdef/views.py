from django.shortcuts import render
from.models import Cartao
import google.generativeai as genai
import PIL.Image
import os

# Create your views here.
def descricao(request):
    return render(request, "descricao.html")

def formulario(request):

    contexto = {}

    if request.method == "POST":
        #Recebe os dados do formulário
        remetente = request.POST.get("remetente")
        print(remetente)

        contexto = {}

        #Código para salvar a imagem
        if "imagem" in request.FILES:
            cartao = Cartao()

            cartao.imagem = request.FILES["imagem"]
            cartao.remetente = remetente

            cartao.save()
            
            #Código para enviar a imagem para a IA
            GOOGLE_API_KEY = "AIzaSyCrJHeuVlhGitTdgmnlDY_i7ETfiRMFTC0"

            genai.configure(api_key=GOOGLE_API_KEY)

            model = genai.GenerativeModel("gemini-1.5-flash")
            imagemCarregada = PIL.Image.open(cartao.imagem)
            response = model.generate_content(["Gere um texto descrevendo a imagem para uma pessoa cega: \n", imagemCarregada])
            print(response.text),

            mensagem = response.text

        contexto = {
            "remetente": remetente,
            "resposta": response.text,
        }

    return render(request, "formulario.html", contexto)