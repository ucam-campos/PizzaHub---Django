#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import CadastroMateriais
from django import forms

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

#Seixas - commit
#TODO - inserir em outro App? separar Estoque(onde teremos cadastro) da Entrega(onte temos pedidos, clientes, etc)?
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('cadastroconfirmado.html', form.cleaned_data)    
    else:
        form = ClienteForm()                    
    vars = {'form':form}
    return render_to_response('cadastro.html', vars)

def listar_pizza(request):
    pizzas = Pizza.objects.all()
    vars = {'pizzas':pizzas}
    return render_to_response('pizzas.html', vars)
    
def ver_pedido(request):
    msg = pedido = None
    idPedido = request.GET.get('id_pedido')
    if idPedido:
        try:
            pedido = Pedido.objects.get(id=idPedido)
        except Pedido.DoesNotExist:
            msg = u'Não existe pedido #%s' % idPedido
    vars = {'pedido':pedido, 'msg':msg}
    return render_to_response('pedido.html', vars)

#Seixas - end commit
