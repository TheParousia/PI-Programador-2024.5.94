from django.db import models

# Create your models here.
class Cartao(models.Model):
    imagem = models.ImageField(upload_to="imagens", default="")