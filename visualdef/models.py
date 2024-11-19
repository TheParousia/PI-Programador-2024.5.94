from django.db import models

# Create your models here.
class Cartao(models.Model):
    imagem = models.ImageField(upload_to="imagens", default="")
    mensagem = models.TextField(default="",null=True)
    
class Meumodelo(models.Model):
    imagem = models.ImageField(upload_to='imagens/')
    remetente=models.TextField(default="", null=True)
    destinatario=models.TextField(default="", null = True)
    mensagem=models.TextField(default="", null=True)
