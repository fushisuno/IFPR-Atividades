# Generated by Django 5.0.7 on 2024-08-02 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0003_professor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplina',
            name='alunos',
        ),
        migrations.DeleteModel(
            name='Matricula',
        ),
    ]
