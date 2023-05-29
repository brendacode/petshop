# Generated by Django 4.2 on 2023-04-22 20:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('petshopapp', '0013_petshopapp_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procedimento',
            fields=[
                ('id_procedimento', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('banho', models.CharField(max_length=255)),
            ],
        ),
    ]
