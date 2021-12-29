from django.db import models
from django.contrib.auth.models import User


class Administrator(User):
    class Meta:
        verbose_name = "Administrator"
        verbose_name_plural = "Administrators"

    def __str__(self):
        return "Adm - " + self.get_full_name()
