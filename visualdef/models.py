from django.db import models

# Create your models here.
class Cartao(models.Model):
    imagem = models.ImageField(upload_to="imagems",default='')
    remetente = models.TextField(default="",null=True)
    destinatario = models.TextField(default="",null=True)
    mensagem = models.TextField(default="",null=True)
    