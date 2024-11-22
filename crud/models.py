from django.db import models

# Create your models here.
class Auto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_combustible = models.CharField(max_length=20, choices=[('Gasolina', 'Gasolina'), ('Diesel', 'Diesel'), ('Eléctrico', 'Eléctrico')])
    kilometraje = models.PositiveIntegerField() 

def __str__(self):
    return self.name
