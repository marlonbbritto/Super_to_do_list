from datetime import datetime
from django.db import models

class Tarefas(models.Model):
    user = models.TextField(max_length=100,null=False,blank=False)
    task= models.TextField(max_length=100,null=False,blank=False)
    deadline = models.DateField(default=datetime.now,blank=False)
    status = models.BooleanField(default=True)
    done = models.BooleanField(default=False)
    data_atualizacao_concluida = models.DateField(null=True,blank=True)

    

    def __str__(self):
        return self.task