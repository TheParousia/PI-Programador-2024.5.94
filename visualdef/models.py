from django.db import models
class Meumodelo(models.Model):
    imagem = models.ImageField(upload_to='imagens/')
    remetente=models.TextField(default="", null=True)
    destinatario=models.TextField(default="", null = True)
    mensagem=models.TextField(default="", null=True)
