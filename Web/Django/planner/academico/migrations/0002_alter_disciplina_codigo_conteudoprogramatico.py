# Generated by Django 5.1.3 on 2024-11-08 22:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("academico", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="disciplina",
            name="codigo",
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.CreateModel(
            name="ConteudoProgramatico",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descricao", models.TextField(null=True)),
                (
                    "disciplina",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="conteudos_programaticos",
                        to="academico.disciplina",
                    ),
                ),
            ],
        ),
    ]
