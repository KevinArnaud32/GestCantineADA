from django.db import models


# Create your models here.
class Plat(models.Model):

    name = models.CharField(max_length=180)
    summary = models.CharField(max_length=180)

    class Meta:
        verbose_name = 'Plat'
        verbose_name_plural = 'Plats'

    def __str__(self):
        return self.name