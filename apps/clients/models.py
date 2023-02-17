from django.db import models


class Client(models.Model):
    name = models.CharField('Nome', max_length=100)  # noqa: E501
    email = models.EmailField('E-Mail', max_length=100, unique=True)  # noqa: E501
    cpf = models.CharField('CPF', blank=True, null=True, max_length=11, unique=True)  # noqa: E501
    cnpj = models.CharField('CNPJ', blank=True, null=True, max_length=14, unique=True)  # noqa: E501
    first_phone = models.CharField('Telefone', max_length=50, null=True, blank=True)  # noqa: E501
    second_phone = models.CharField('Telefone 2', max_length=50, null=True, blank=True)  # noqa: E501

    def __str__(self):
        return self.name
