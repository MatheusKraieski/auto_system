from django.db import models

from apps.cars.models import Car
from apps.clients.models import Client


class Service(models.Model):
    ref_code = models.CharField(
        max_length=255, null=False, default=1, blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=1, related_name='Client')  # noqa: E501
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='Carro')  # noqa: E501
    description = models.TextField('Descrição', null=True, blank=True)
    observation = models.TextField('Observações', null=True, blank=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.pk


class ServiceImage(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='images', verbose_name='service')  # noqa: E501
    image = models.ImageField(
        'Imagem', upload_to='uploads/service', max_length=100, null=True, blank=True)  # noqa: E501

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'Imagens'

    def __str__(self):
        return self.product.name
