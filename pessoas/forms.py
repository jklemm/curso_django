# coding: utf-8
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from django import forms


class FormPessoa(forms.Form):
    nome = forms.CharField()
    idade = forms.IntegerField()
