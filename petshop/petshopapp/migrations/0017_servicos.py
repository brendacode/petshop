# Generated by Django 4.2 on 2023-04-27 15:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('petshopapp', '0016_cadastro_produtos_remove_petshopapp_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id_petshop', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('preco', models.CharField(max_length=50)),
            ],
        ),
    ]
