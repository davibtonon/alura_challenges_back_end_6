from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Modelo para salvar os pets.
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
   pet_adotado = models.BooleanField()
   foto_pet = models.FileField(upload_to=None, max_length=100)
   
# Modelo que salvar as messagem dos clientes
class MessagemClientes(models.Model):
   nome = models.CharField(max_length=100)
   telefone = models.CharField( max_length=14)
   nome_animal = models.ForeignKey(Pets, on_delete=models.PROTECT)
   mensagem = models.CharField(max_length=300)
   respondida = models.BooleanField()

# Modelos para salvas dados personalizados de cada usuarios
class DadosPersonalizadosUsuarios(models.Model):

   user = models.ForeignKey(User, on_delete=models.PROTECT)
   telefone = telefone = models.CharField( max_length=14)
   cidade = models.CharField(max_length=200)
   sobre = models.CharField(max_length=400)
   foto_perfil = models.FileField()