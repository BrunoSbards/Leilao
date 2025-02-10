from django.db import models

class leiloeiro(models.Model):
    
    leiloeiro_nome = models.CharField(primary_key=True, max_length=100, default='')
    leiloeiro_cpf = models.CharField(max_length=150, default='')
    leiloeiro_email = models.EmailField(default='')
    leiloeiro_fone = models.CharField(max_length=150, default='')
    leiloeiro_site = models.URLField(blank=True, null=True)
    matricula = models.ForeignKey("matricula", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.leiloeiro_nome
    

class matricula(models.Model):
    numero_matricula = models.CharField(max_length=20, unique=True)
    estado_matricula = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.numero_matricula
    

class Estado(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.nome

class Anexo(models.Model):
    leiloeiro = models.ForeignKey(leiloeiro, on_delete=models.CASCADE)
    matricula = models.ForeignKey(matricula, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to="anexos/")

    def __str__(self):
        return f"Anexo de {self.leiloeiro.username} - {self.arquivo.name}"        

    

       