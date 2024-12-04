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
                ('imagem', models.ImageField(default='', upload_to='imagens')),
                ('mensagem', models.TextField(default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meumodelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='imagens/')),
                ('remetente', models.TextField(default='', null=True)),
                ('destinatario', models.TextField(default='', null=True)),
                ('mensagem', models.TextField(default='', null=True)),
            ],
        ),
    ]
