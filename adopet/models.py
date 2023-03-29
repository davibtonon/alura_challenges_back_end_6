from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pets(models.Model):
   tamanho_pet = (
      "Pequeno",
      "Medio",
      "Grande"
   )

   nome = models.CharField(max_length=50)
   idade = models.IntegerField()
   porte = models.Choices(tamanho_pet)
   dono = models.ForeignKey(User, on_delete=models.PROTECT)
   # Descobrir como posso add uma lista de personalidades.
   personalidades = models.models.CharField(max_length=150)
   endereco = models.CharField(max_length=200)
   
