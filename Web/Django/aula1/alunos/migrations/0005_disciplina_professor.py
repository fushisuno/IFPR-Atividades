# Generated by Django 5.0.7 on 2024-08-02 23:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0004_remove_disciplina_alunos_delete_matricula'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='alunos.professor'),
        ),
    ]
