from django.db import models

class Item(models.Model):
  nome = models.CharField('Nome', max_length=100, null=False, 
  unique=True)
  estoque = models.PositiveIntegerField('Estoque', blank=False,      default=0)
  estoque_min = models.PositiveIntegerField('Estoque Min',           blank=False, default=0)
  slug = models.SlugField('Atalho')

def __str__(self):
    return self.nome