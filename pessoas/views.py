from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


from pessoas.forms import FormPessoa
from pessoas.models import Pessoa


class ListarPessoasView(View):
    def get(self, request):
        pessoas = Pessoa.objects.all()
        return render(request, 'listar_pessoas.html', {'pessoas': pessoas})

    def post(self, request):
        return HttpResponse('post')


class CadastrarPessoaView(View):
    def get(self, request):
        form = FormPessoa()
        return render(request, 'cadastrar_pessoa.html', {'form': form})

    def post(self, request):

        form = FormPessoa(request.POST)

        if not form.is_valid():
            return render(request, 'cadastrar_pessoa.html', {'form': form})

        nome = form.cleaned_data['nome']
        idade = form.cleaned_data['idade']

        # forma 1
        # Pessoa.objects.create(nome=nome, idade=idade)

        # forma 2
        pessoa = Pessoa()
        pessoa.nome = nome
        pessoa.idade = idade
        pessoa.save()

        return redirect(reverse('listar_pessoas'))


class AlterarPessoaView(View):
    def get(self, request, pessoa_id=None):
        return HttpResponse('AlterarPessoaView -> get : pessoa_id: {}'.format(pessoa_id))

    def post(self, request):
        return HttpResponse('AlterarPessoaView -> post')


class ExcluirPessoaView(View):
    def get(self, request, pessoa_id=None):
        return HttpResponse('ExcluirPessoaView -> get : pessoa_id: {}'.format(pessoa_id))

    def post(self, request):
        return HttpResponse('ExcluirPessoaView -> post')
