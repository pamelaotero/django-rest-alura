from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9) 
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    # black para nao permitir que o curso não tenha um nível e não podem ser null
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    # Um curso seja representado por sua descrição
    def __str__(self):
        return self.descricao
