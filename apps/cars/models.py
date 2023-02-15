from django.db import models

class Car(models.Model):
    name = models.CharField('Nome', max_length=100)
    brand = models.CharField('Marca', max_length=100)
    plate = models.CharField('Placa', max_length=100, unique=True)
    year = models.IntegerField('Ano', blank=True, null=True, max_length=11, unique=True)
    km = models.CharField('Quilometro', blank=True, null=True, max_length=14, unique=True)
    color = models.CharField('Cor', max_length=50, null=True, blank=True)
    

    def __str__(self):
        return self.name
