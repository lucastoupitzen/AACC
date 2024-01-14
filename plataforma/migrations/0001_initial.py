# Generated by Django 4.1.6 on 2024-01-10 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AACC",
            fields=[
                ("id_aacc", models.AutoField(primary_key=True, serialize=False)),
                ("aluno", models.CharField(max_length=8)),
                ("doc", models.FileField(upload_to="documentos/")),
                ("data_envio", models.DateField()),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (0, "Aguardando"),
                            (1, "Enviada"),
                            (2, "Avaliada"),
                            (3, "Confirmada"),
                        ],
                        default=0,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "nrousp",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("nome", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=50)),
                (
                    "cargo",
                    models.CharField(
                        choices=[
                            ("professor", "Professor"),
                            ("coordenador", "Coordenador"),
                        ],
                        default="professor",
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Login",
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
                ("senha_hash", models.CharField(max_length=255)),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="plataforma.usuario",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AACC_para_avaliacao",
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
                (
                    "id_aacc",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="plataforma.aacc",
                    ),
                ),
                (
                    "id_avaliador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="plataforma.usuario",
                    ),
                ),
            ],
        ),
    ]