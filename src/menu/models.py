from django.db import models
from plat.models import Plat

# Create your models here.
class Menu(models.Model):

    plat = models.OneToOneField(Plat, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'