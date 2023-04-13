from django.db import models

# Modelo de aluno
class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    
    def __str__(self):
        return self.nome

# Modelo de curso
class Curso(models.Model):
    
    NIVEL = (
        ('B','Báeico'),
        ('I','Intermediário'),
        ('A','Avançado'),
    )
    
    codigo_curso = models.CharField(max_length=8)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1,choices=NIVEL, blank=False, null=False, default='B')
    
    def __str__(self):
        return self.descricao

# Modelo de Matricula
class Matricula(models.Model):
    
    PERIODO = (
        ('M','Matutino'),
        ('V','Verpertino'),
        ('N','Noturno'),
    )
    
    codigo_matricula = models.CharField(max_length=8)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1,choices=PERIODO, blank=False, null=False, default='M')