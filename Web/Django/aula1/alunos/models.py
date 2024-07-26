from django.db import models

# Create your models here.
class Aluno(models.Model):
  nome = models.CharField(max_length=200)
  data_nascimento = models.DataField()

class Curso(models.Model):
  nome = models.CharField(max_length=200)

  def __str__(self):
    return self.nome

class Diciplina(models.Model):
  curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
  nome = models.CharField(max_length=200)
  codigo = models.CharField(max_length=6, null=True)