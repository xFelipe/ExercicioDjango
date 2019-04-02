from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=15, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome
