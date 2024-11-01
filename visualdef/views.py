from django.shortcuts import render
import google.generativeai as genai
import PIL.Image
import os

# Create your views here.
def formulario(request):

    contexto = {}
    if request.method == "POST":
        remetente = request.GET.get("remetente")
        print(remetente)

        contexto = {}

        if remetente is not None:
            GOOGLE_API_KEY = "AIzaSyCrJHeuVlhGitTdgmnlDY_i7ETfiRMFTC0"

            genai.configure(api_key=GOOGLE_API_KEY)

            model = genai.GenerativeModel("gemini-1.5-flash")
            imagemCarregada = PIL.Image.open(cartao.imagem)
            response = model.generate_content(remetente)
            print(response.text),

            mensagem = response.text

        contexto = {
            "remetente": remetente,
            "resposta": response.text
        }

    return render(request, "formulario.html", contexto)