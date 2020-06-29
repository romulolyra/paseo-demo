from .forms import UserForm
from .models import NovoUser
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect


def inicial(request):
    usuarios = NovoUser.objects.all()
    return render(request, 'app/inicial.html',{'usuarios':usuarios})

def sobre(request):
    return render(request, 'app/sobre.html')

def log(request):
    return render(request, 'app/login.html')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        #foto = request.FILES['foto']
        email = request.POST['email']
        senha1 = request.POST['senha1']
        senha2 = request.POST['senha2']
        largadouro = request.POST['largadouro']
        numero = request.POST['numero']
        cep = request.POST['cep']
        curso = request.POST['curso']

        #carro :
        placa = request.POST['placa']
        cor = request.POST['cor']
        modelo = request.POST['modelo']

        #interesses :
        e1 = request.POST['e1']
        e2 = request.POST['e2']
        e3 = request.POST['e3']
        e4 = request.POST['e4']

        r1 = request.POST['r1']
        r2 = request.POST['r2']
        r3 = request.POST['r3']
        r4 = request.POST['r4']

        j1 = request.POST['j1']
        j2 = request.POST['j2']
        j3 = request.POST['j3']
        j4 = request.POST['j4']
        j5 = request.POST['j5']
        j6 = request.POST['j6']

        a1 = request.POST['a1']
        a2 = request.POST['a2']
        a3 = request.POST['a3']
        a4 = request.POST['a4']
        a5 = request.POST['a5']
        a6 = request.POST['a6']

        s1 = request.POST['s1']
        s2 = request.POST['s2']
        s3 = request.POST['s3']
        s4 = request.POST['s4']

        h1 = request.POST['h1']
        h2 = request.POST['h2']
        h3 = request.POST['h3']
        h4 = request.POST['h4']
        h5 = request.POST['h5']
        h6 = request.POST['h6']

        so1 = request.POST['so1']
        so2 = request.POST['so2']
        so3 = request.POST['so3']
        so4 = request.POST['so4']







        # relacionar os inputs do html com o modelo no banco de dados :
        usuario = NovoUser.objects.create(
            nome = nome,
            sobrenome = sobrenome,
            #foto = foto,
            email = email,
            senha1 = senha1,
            senha2 = senha2,
            largadouro = largadouro,
            numero = numero,
            cep = cep,
            curso = curso,
            placa = placa,
            cor = cor,
            modelo = modelo,
            e1 = e1,
            e2 = e2,
            e3 = e3,
            e4 = e4,
            r1 = r1,
            r2 = r2,
            r3 = r3,
            r4 = r4,
            j1 = j1,
            j2 = j2,
            j3 = j3,
            j4 = j4,
            j5 = j5,
            j6 = j6,
            a1 = a1,
            a2 = a2,
            a3 = a3,
            a4 = a4,
            a5 = a5,
            a6 = a6,
            s1 = s1,
            s2 = s2,
            s3 = s3,
            s4 = s4,
            h1 = h1,
            h2 = h2,
            h3 = h3,
            h4 = h4,
            h5 = h5,
            h6 = h6,
            so1 = so1,
            so2 = so2,
            so3 = so3,
            so4 = so4,

        )
        usuario.save()

        return HttpResponseRedirect('/inicial')

    else:
       print('mesmo erro')


    return render(request, 'app/cadastro.html')

