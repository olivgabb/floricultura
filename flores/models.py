from django.db import models

# Create your models here.

class Planta(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    categoria = models.CharField(max_length=255)
    image_url = models.TextField(default="")