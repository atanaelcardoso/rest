from django.db import models
#from django.contrib.auth import get_user_model

class Cliente(models.Model):
  nome = models.CharField(max_length=50)
  endereco = models.CharField(max_length=50)
  idade = models.IntegerField()
 # user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

  def __str__(self):
    return self.name

