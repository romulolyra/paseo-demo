from django.db import models
import requests

class User(models.Model):

    CURSOS = (
        ('cc','Ciências da computação'),
        ('ds','Design'),
    )
    nome = models.CharField(max_length=100)
    #foto = models.ImageField()
    email = models.EmailField()
    endereco = models.CharField(max_length=200)
    cep = models.CharField(max_length=10)
    curso = models.CharField(
        max_length= 25,
        choices=CURSOS,
    )

class NovoUser(models.Model):




    def __str__(self):
        return self.nome
    CURSOS = (
        ('cc','Ciências da computação'),
        ('ds','Design'),
    )
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    foto = models.ImageField()
    email = models.EmailField()
    senha1 = models.CharField(max_length=50)
    senha2= models.CharField(max_length=50)
    largadouro = models.CharField(max_length=200)
    numero =  models.CharField(max_length=10)
    cep = models.CharField(max_length=10)
    curso = models.CharField(
        max_length= 25,
        choices=CURSOS,
    )
    #*** carro ***
    placa = models.CharField(max_length=9)
    cor = models.CharField(max_length=19)
    modelo =  models.CharField(max_length=19)
    #-- indices reservas caso deseje adicionar algum sem mudar a estrutura de dados:
    reserva1 = models.CharField(max_length=50)
    reserva2 = models.CharField(max_length=50)

    # **** interesses: *****

    #  esportes
    e1 = models.BooleanField(default=False)
    e2 = models.BooleanField(default=False)
    e3 = models.BooleanField(default=False)
    e4 = models.BooleanField(default=False)

    # reality shows
    r1 = models.BooleanField(default=False)
    r2 = models.BooleanField(default=False)
    r3 = models.BooleanField(default=False)
    r4 = models.BooleanField(default=False)

    #  jogos
    j1 = models.BooleanField(default=False)
    j2 = models.BooleanField(default=False)
    j3 = models.BooleanField(default=False)
    j4 = models.BooleanField(default=False)
    j5 = models.BooleanField(default=False)
    j6 = models.BooleanField(default=False)

    # animes
    a1 = models.BooleanField(default=False)
    a2 = models.BooleanField(default=False)
    a3 = models.BooleanField(default=False)
    a4 = models.BooleanField(default=False)
    a5 = models.BooleanField(default=False)
    a6 = models.BooleanField(default=False)

    # streaming
    s1 = models.BooleanField(default=False)
    s2 = models.BooleanField(default=False)
    s3 = models.BooleanField(default=False)
    s4 = models.BooleanField(default=False)

    #hobbies
    h1 = models.BooleanField(default=False)
    h2 = models.BooleanField(default=False)
    h3 = models.BooleanField(default=False)
    h4 = models.BooleanField(default=False)
    h5 = models.BooleanField(default=False)
    h6 = models.BooleanField(default=False)

    #sobre voce
    so1 = models.BooleanField(default=False)
    so2 = models.BooleanField(default=False)
    so3 = models.BooleanField(default=False)
    so4 = models.BooleanField(default=False)

    #categoria vazia caso seja preciso adicionar mais uma
    v1 = models.BooleanField(default=False)
    v2 = models.BooleanField(default=False)
    v3 = models.BooleanField(default=False)
    v4 = models.BooleanField(default=False)
    v5 = models.BooleanField(default=False)
    v6 = models.BooleanField(default=False)

