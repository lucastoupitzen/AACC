# Generated by Django 4.1.6 on 2024-01-15 16:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "plataforma",
            "0002_alter_aacc_para_avaliacao_id_avaliador_delete_login_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="aacc_para_avaliacao",
            name="comentarios",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="aacc_para_avaliacao",
            name="status",
            field=models.IntegerField(
                choices=[(0, "Aguardando"), (1, "Deferida"), (2, "Indeferida")],
                default=0,
            ),
        ),
    ]
