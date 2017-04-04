# coding: utf-8
from django.db import models

'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
'''

class CadastroMateriais(models.Model):
    nome = models.CharField(max_length=200)
    quantidade = models.IntegerField(default=0)
    preco = models.IntegerField(default=0)
    numeronf = models.IntegerField(default=0)
    
#Seixas - commit
DDD_PADRAO = u'22'

SABORES = [
    ('calabresa' ,u'Calabresa'),
    ('catupiry' ,u'Catupiry'),
    ('mussarela' ,u'Mussarela'),
    ('portuguesa' ,u'Portuguesa'),
    ('quatro queijos' ,u'Quatro Queijos'),
]

class Cliente(models.Model):
    ddd = models.CharField(max_length=2, default=DDD_PADRAO)
    fone = models.CharField(max_length=9, db_index=True)
    contato = models.CharField(max_length=86, db_index=True)
    logradouro = models.CharField(max_length=64, db_index=True)
    numero = models.PositiveIntegerField(u'número', db_index=True)
    complemento = models.CharField(max_length=32, blank=True)
    obs = models.TextField(blank=True)
    
    class Meta:  # usar admin? ordenação pensando nisso
        unique_together = ['ddd', 'fone']
        ordering = ['fone', 'ramal'] 
        
    def __unicode__(self):
        fone = self.fone
        if self.ddd != DDD_PADRAO:
            fone = u'(%s)%s' % (self.ddd, fone)
        return u'%s - %s' % (fone, self.contato)

    def endereco(self):
        end = u'%s, %s' % (self.logradouro, self.numero)
        if self.complemento:
            end += u', ' + self.complemento
        return end
    endereco.short_description = u'endereço'
    
class Pedido(models.Model):
    inclusao = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente)
    partida = models.TimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-inclusao']
    
    def __unicode__(self):
        return u'%s / %s' % (self.entrou(), self.cliente)

    def entrou(self):
	#tempo de entrada
        return self.inclusao.strftime('%H:%M')

    def partiu(self):
	#tempo de partida
        if self.partida:
            return self.partida.strftime('%H:%M')
        else:
            return ''

    def despachado(self):
        return (self.partida is not None)
    despachado.boolean = True    

    
class Pizza(models.Model):
    pedido = models.ForeignKey(Pedido)
    sabor1 = models.CharField(u'sabor 1', max_length=32, choices=SABORES)
    sabor2 = models.CharField(u'sabor 2', max_length=32, choices=SABORES, blank=True)

    def __unicode__(self):
        sabor = self.sabor1
        if self.sabor2:
            sabor2 = self.sabor2
            sabor = u'½ %s, ½ %s' % (sabor, sabor2) 
        return sabor
#Seixas - end commit
