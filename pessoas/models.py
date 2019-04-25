from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=255, blank=False, name="Nome", help_text="Informe aqui o nome da pessoa")
    idade = models.IntegerField(name="Idade", help_text="Informe a idade da pessoa")
