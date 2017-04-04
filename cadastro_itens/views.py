#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import CadastroMateriais


def Cadastar(request):
    if request.method == 'POST':
        name = request.POST.get('nomepro')
        quant = request.POST.get('quantidade')
        val = request.POST.get('preco')
        valnf = request.POST.get('nfval')

        if not name:
            return render(request, 'deletar.html',
                          {'reto': 'Nome em branco'})
        elif not quant:
            return render(request, 'deletar.html',
                          {'reto': 'Quantidade em branco'})
        elif not val:
            return render(request, 'deletar.html',
                          {'reto': 'Valor em branco'})
        elif not valnf:
            return render(request, 'deletar.html',
                          {'reto': 'NF em branco'})
        else:
            CadastroMateriais.objects.create(nome=name,
                    quantidade=quant, preco=val)
            return render(request, 'cadastro.html',
                          {'reto': 'Iten cadastrado'})

    return render(request, 'cadastro.html')


def Apagar(request):
    aid = request.GET.get('iten_id')
    iten = CadastroMateriais.objects.get(id=aid)
    if request.method == 'POST':
        CadastroMateriais.objects.get(id=aid).delete()
        return render(request, 'deletar.html', {'reto': 'Iten apagado'})

    return render(request, 'deletar.html', {'itens': iten})


def MostarValores(request):
    if request.method == 'GET':
        lista_itens = CadastroMateriais.objects.all()

    return render(request, 'mostrar.html', {'lista_itens': lista_itens})



			