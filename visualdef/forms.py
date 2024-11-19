from django import forms
from .models import Meumodelo

class MeuFormulario(forms.ModelForm):
    class Meta:
        model = Meumodelo
        fields = ('imagem',)