from django.db import models
from django.contrib.auth.models import User



class AACC(models.Model):

    STATUS_CHOICES = [
        (0, 'Aguardando'),
        (1, 'Enviada'),
        (2, 'Avaliada'),
        (3, 'Confirmada'),
    ]

    id_aacc = models.AutoField(primary_key=True)
    aluno = models.CharField(max_length=8)
    doc = models.FileField(upload_to='documentos/')
    data_envio = models.DateField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return f"AACC {self.id_aacc} - Aluno : {self.aluno}"
    
class AACC_para_avaliacao(models.Model):

    id_avaliador = models.ForeignKey(User, on_delete=models.CASCADE)
    id_aacc = models.ForeignKey(AACC, on_delete=models.CASCADE)

    def __str__(self):
        return f"AACC {self.id_aacc.id_aacc} - {self.id_avaliador.username}"