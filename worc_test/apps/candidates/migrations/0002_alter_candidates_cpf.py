# Generated by Django 3.2.7 on 2021-12-27 18:43

import cpf_field.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("candidates", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidates",
            name="cpf",
            field=cpf_field.models.CPFField(max_length=14, unique=True),
        ),
    ]
