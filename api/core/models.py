from django.db import models
from pro.models import Produto

class Cliente(models.Model):
  nome = models.CharField(max_length=50)
  endereco = models.CharField(max_length=50)
  idade = models.IntegerField()
  pro = models.ForeignKey(Produto, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

