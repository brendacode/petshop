# Generated by Django 4.2 on 2023-04-22 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petshopapp', '0007_rename_author_petshopapp_endereco'),
    ]

    operations = [
        migrations.RenameField(
            model_name='petshopapp',
            old_name='state',
            new_name='nome_do_pet',
        ),
    ]