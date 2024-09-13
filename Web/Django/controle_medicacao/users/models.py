from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_user = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefone = models.CharField(max_length=13)
    senha = models.CharField(max_length=200)

class Medicamento(models.Model):
    id_medc = models.BigAutoField(primary_key=True)
    nome_medicamento = models.CharField(max_length=200)
    dosagem = models.CharField(max_length=50)
    forma = models.CharField(max_length=100)
    

class Prescricao(models.Model):
    id_presc = models.BigAutoField(primary_key=True)
    id_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_medc = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    freq_uso = models.CharField(max_length=200)

    
class Registro(models.Model):
    id_reg = models.BigAutoField(primary_key=True)
    id_presc = models.ForeignKey(Prescricao, on_delete=models.CASCADE)
    data_prev = models.DateField()
    hora_prev = models.DateTimeField()
    data_toma = models.DateField()
    hora_toma = models.DateTimeField()
    obs = models.TextField()