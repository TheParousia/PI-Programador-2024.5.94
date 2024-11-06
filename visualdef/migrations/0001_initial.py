# Generated by Django 4.2.16 on 2024-11-06 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(default='', upload_to='imagems')),
                ('remetente', models.TextField(default='', null=True)),
                ('destinatario', models.TextField(default='', null=True)),
                ('mensagem', models.TextField(default='', null=True)),
            ],
        ),
    ]
