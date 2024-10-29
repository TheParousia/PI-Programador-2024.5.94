from django.shortcuts import render
import google.generativeai as genai
import os

# Create your views here.
def descricao(request):


        remetente = request.GET.get("remetente")
        print(remetente)

        contexto = {}

        if remetente is not None:
                
                genai.configure(api_key="AIzaSyCrJHeuVlhGitTdgmnlDY_i7ETfiRMFTC0")

                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(remetente)
                print(response.text),

                contexto = {
                "remetente": remetente,
                "resposta": response.text
                }

        return render(request, "formulario.html", contexto)