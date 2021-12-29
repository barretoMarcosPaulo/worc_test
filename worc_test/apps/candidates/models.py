from django.db import models
from django.core.validators import MinValueValidator

from cpf_field.models import CPFField


class Candidates(models.Model):
    name = models.CharField(max_length=156, blank=False, null=False)
    email = models.CharField(max_length=156, blank=False, null=False, unique=True)
    cpf = CPFField(unique=True, blank=True, null=True)
    age = models.PositiveIntegerField("Idade", validators=[MinValueValidator(19)])
    salary_claim = models.DecimalField(max_digits=13, decimal_places=2)
    immediate_availability = models.BooleanField(blank=False, null=False)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.name
