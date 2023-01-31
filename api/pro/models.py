from django.db import models

class Produto(models.Model):
  nome = models.CharField(max_length=50)
  descricao = models.TextField()
  quantidade = models.DecimalField(max_digits=10, decimal_places=3)
  custo = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return self.name
