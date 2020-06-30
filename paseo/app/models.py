from django.db import models
import requests
#modelo de usuário da primeira versão:
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
#modelo de usuário da segunda versão:
class NovoUser(models.Model):
    def __str__(self):
        return self.nome
    CURSOS = (
        ('Ciências da computação','Ciências da computação'),
        ('Design','Design'),
    )

    #funçao que busca informações da localização da pessoa pelo CEP a partir da API ViaCEP

    def via_cep(cep):
        info = requests.get("https://viacep.com.br/ws/" + str(cep) + "/json/")
        return (info.json()['bairro'])



    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    foto = models.ImageField() #Framework pode pedir uma extenção adicinal para lidar com arquivos estáticos
    email = models.EmailField()
    senha1 = models.CharField(max_length=50)
    senha2 = models.CharField(max_length=50)
    largadouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    cep = models.CharField(max_length=10)
    curso = models.CharField(
        max_length=25,
        choices=CURSOS,
    )
    # *** carro ***
    #foi necessário indicar valores padrões para caso o usuário não digite nenhuma opção
    placa = models.CharField(max_length=9, null=True, blank=True)
    cor = models.CharField(max_length=19, null=True, blank=True)
    modelo = models.CharField(max_length=19, null=True, blank=True)
    # -- indices reservas caso deseje adicionar algum sem mudar a estrutura de dados:
    reserva1 = models.CharField(max_length=50, null=True, blank=True)
    reserva2 = models.CharField(max_length=50, null=True, blank=True)

    # **** interesses: *****

    #  esportes
    e1 = models.BooleanField(default=False, blank=False)
    e2 = models.BooleanField(default=False, blank=False)
    e3 = models.BooleanField(default=False, blank=False)
    e4 = models.BooleanField(default=False, blank=False)

    # reality shows
    r1 = models.BooleanField(default=False, blank=False)
    r2 = models.BooleanField(default=False, blank=False)
    r3 = models.BooleanField(default=False, blank=False)
    r4 = models.BooleanField(default=False, blank=False)

    #  jogos
    j1 = models.BooleanField(default=False, blank=False)
    j2 = models.BooleanField(default=False, blank=False)
    j3 = models.BooleanField(default=False, blank=False)
    j4 = models.BooleanField(default=False, blank=False)
    j5 = models.BooleanField(default=False, blank=False)
    j6 = models.BooleanField(default=False, blank=False)

    # animes
    a1 = models.BooleanField(default=False, blank=False)
    a2 = models.BooleanField(default=False, blank=False)
    a3 = models.BooleanField(default=False, blank=False)
    a4 = models.BooleanField(default=False, blank=False)
    a5 = models.BooleanField(default=False, blank=False)
    a6 = models.BooleanField(default=False, blank=False)

    # streaming
    s1 = models.BooleanField(default=False, blank=False)
    s2 = models.BooleanField(default=False, blank=False)
    s3 = models.BooleanField(default=False, blank=False)
    s4 = models.BooleanField(default=False, blank=False)

    # hobbies
    h1 = models.BooleanField(default=False, blank=False)
    h2 = models.BooleanField(default=False, blank=False)
    h3 = models.BooleanField(default=False, blank=False)
    h4 = models.BooleanField(default=False, blank=False)
    h5 = models.BooleanField(default=False, blank=False)
    h6 = models.BooleanField(default=False, blank=False)

    # sobre voce
    so1 = models.BooleanField(default=False, blank=False)
    so2 = models.BooleanField(default=False, blank=False)
    so3 = models.BooleanField(default=False, blank=False)
    so4 = models.BooleanField(default=False, blank=False)

    # categoria vazia caso seja preciso adicionar mais uma
    v1 = models.BooleanField(default=False, blank=False)
    v2 = models.BooleanField(default=False, blank=False)
    v3 = models.BooleanField(default=False, blank=False)
    v4 = models.BooleanField(default=False, blank=False)
    v5 = models.BooleanField(default=False, blank=False)
    v6 = models.BooleanField(default=False, blank=False)



