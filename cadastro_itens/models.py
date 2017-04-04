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
    
