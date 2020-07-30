from django.db import models


# Create your models here.

class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    SIM = 'SIM'
    NAO = 'NAO'
    urgencia_escolhas = [
        (SIM, 'SIM'),
        (NAO, 'NAO'),
    ]
    urgencia = models.CharField(
        max_length=3,
        choices=urgencia_escolhas,
        default=NAO,
    )


    class Meta:
        verbose_name_plural = 'Tarefas'

    def __str__(self):
        return self.nome