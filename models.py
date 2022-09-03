from django.db import models

# Create your models here.

Class Remeras(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_ingreso = models.DateField()
    stock_remera = models.IntegerField

Class EstiloRemera(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_lanzamiento = models.DateField()
    remera = models.ForeignKey('Remeras', on_delete=models.CASCADE)