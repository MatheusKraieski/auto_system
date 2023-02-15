# Generated by Django 4.1.7 on 2023-02-15 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('brand', models.CharField(max_length=100, verbose_name='Marca')),
                ('plate', models.CharField(max_length=100, unique=True, verbose_name='Placa')),
                ('year', models.DecimalField(blank=True, decimal_places=4, max_digits=4, null=True)),
                ('km', models.CharField(blank=True, max_length=14, null=True, verbose_name='Quilometro')),
                ('color', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cor')),
            ],
        ),
    ]
