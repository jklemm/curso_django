# Generated by Django 2.2 on 2019-05-09 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0002_pessoa_ultima_alteracao'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
    ]
