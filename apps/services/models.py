from django.db import models
from apps.clients.models import Client
from apps.cars.models import Car


class Service(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='services')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='services')
    description = models.TextField('Descrição', null=True, blank=True)
    observation = models.TextField('observações', null=True, blank=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.pk


class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='images', verbose_name='service')
    image = models.ImageField('Imagem', upload_to='uploads/service', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'Imagens'

    def __str__(self):
        return self.product.name