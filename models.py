from django.db import models

# Create your models here.

Class Remeras(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_lanzamiento = models.DateField()


Class Pantalones(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_lanzamiento = models.DateField()