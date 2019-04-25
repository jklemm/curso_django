# curso_django

Para instalar o ambiente:

1 - Faça o git clone do repositório

2 - Abra o projeto e crie uma virtualenv no PyCharm

3.1 - Abra o arquivo requirements.txt no PyCharm e aperte em atualizar OU

3.2 - Abra o terminal no diretório do projeto e rode o comando: `pip install -r requirements.txt`

4 - Rode o comando para aplicar as migrações: `python manage.py migrate`

5.1 - Rode o comando para rodar o projeto `python manage.py runserver 0.0.0.0:8000` OU

5.2 - Em Run Configurations no Pycharm, configure um Django Server, e aperte o play.

6 - Acesse no navegador: http://localhost:8000 ou http://0.0.0.0:8000
