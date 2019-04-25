from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# FBV
from pessoas.forms import FormPessoa


def listar_pessoas_fbv(request):
    if request.method == 'GET':
        return HttpResponse('get')
    elif request.method == 'POST':
        return HttpResponse('post')


# CBV
class ListarPessoasCBV(View):
    def get(self, request):
        return render(request, 'listar_pessoas.html', {})

    def post(self, request):
        return HttpResponse('post')


class CadastrarPessoaView(View):
    def get(self, request):
        form = FormPessoa()
        return render(request, 'cadastrar_pessoa.html', {'form': form})

    def post(self, request):
        # salvar a pessoa no banco
        return HttpResponse('post')
