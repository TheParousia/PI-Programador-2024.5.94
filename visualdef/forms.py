from django import forms
from .models import MeuModelo

class MeuFormulario(forms.ModelForm):
    class Meta:
        model = MeuModelo
        fields = ('imagem',)