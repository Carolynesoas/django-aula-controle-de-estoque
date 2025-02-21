from django.db import models
class Categorias (models.Model):
    nome = models.CharField(verbose_name='Categorias do produto', blank='false', null='false', max_length=200 )

    class Meta:
        verbose_name = 'Categorias'
        verbose_name_plural = 'Categorias'
        db_table = 'Categorias'

    def __str__(self):
        return self.nome

