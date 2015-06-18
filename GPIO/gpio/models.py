from django.db import models

# Create your models here.
class Nombre(models.Model):
    nombre_text = models.CharField(max_length=50)

    def __str__(self):              # __unicode__ on Python 2
        return self.nombre_text