# Generated by Django 4.2 on 2023-05-05 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petshopapp', '0017_servicos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Petshopapp',
        ),
        migrations.AlterField(
            model_name='servicos',
            name='preco',
            field=models.IntegerField(max_length=50),
        ),
    ]
