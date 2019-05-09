from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=255, blank=False, verbose_name="Nome", help_text="Informe aqui o nome da pessoa")
    idade = models.IntegerField(verbose_name="Idade", help_text="Informe a idade da pessoa")
    excluido = models.BooleanField(default=False)
    ultima_alteracao = models.DateTimeField(null=True)
