# Generated by Django 3.2.7 on 2021-12-27 18:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Candidates",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=156)),
                ("email", models.CharField(max_length=156, unique=True)),
                ("cpf", models.CharField(editable=False, max_length=20, unique=True)),
                (
                    "age",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MinValueValidator(18)],
                        verbose_name="Idade",
                    ),
                ),
                ("salary_claim", models.DecimalField(decimal_places=2, max_digits=13)),
                ("immediate_availability", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Employee",
                "verbose_name_plural": "Employees",
            },
        ),
    ]
