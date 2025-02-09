from django.db import models
from django.contrib.auth.models import AbstractUser

class Estado(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.nome

class Leiloeiro(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    site = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username

class Matricula(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    leiloeiro = models.ForeignKey(Leiloeiro, on_delete=models.CASCADE, related_name="matriculas")

    def __str__(self):
        return f"{self.numero} - {self.estado.sigla}"

class Anexo(models.Model):
    leiloeiro = models.ForeignKey(Leiloeiro, on_delete=models.CASCADE)
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to="anexos/")

    def __str__(self):
        return f"Anexo de {self.leiloeiro.username} - {self.arquivo.name}"
