# Generated by Django 2.2 on 2019-05-07 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Informe aqui o nome da pessoa', max_length=255, verbose_name='Nome')),
                ('idade', models.IntegerField(help_text='Informe a idade da pessoa', verbose_name='Idade')),
            ],
        ),
    ]
