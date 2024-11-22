# Generated by Django 5.0.7 on 2024-10-11 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Prescricao",
            fields=[
                ("id_presc", models.BigAutoField(primary_key=True, serialize=False)),
                ("data_inicio", models.DateField()),
                ("data_fim", models.DateField()),
                ("freq_uso", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                ("id_user", models.BigAutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=200)),
                ("sobrenome", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200)),
                ("telefone", models.CharField(max_length=15)),
                ("senha", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Medicamento",
            fields=[
                ("id_medc", models.BigAutoField(primary_key=True, serialize=False)),
                ("nome_medicamento", models.CharField(max_length=200)),
                ("dosagem", models.CharField(max_length=50)),
                ("forma", models.CharField(max_length=100)),
                (
                    "prescricao",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="medicamentos",
                        to="saude.prescricao",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="prescricao",
            name="id_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="saude.usuario"
            ),
        ),
    ]