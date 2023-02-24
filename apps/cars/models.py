from django.db import models, transaction


class Car(models.Model):
    name = models.CharField('Nome', max_length=100)
    brand = models.CharField('Marca', max_length=100)
    plate = models.CharField('Placa', max_length=100, unique=True)
    year = models.DecimalField(max_digits=4, null=True, blank=True, decimal_places=0)  # noqa: E501
    km = models.CharField('Quilometro', blank=True, null=True, max_length=14)
    color = models.CharField('Cor', max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
