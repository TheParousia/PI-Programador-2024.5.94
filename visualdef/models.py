from django.db import models
class MeuModelo(models.Model):
    imagem = models.ImageField(upload_to='imagens/')