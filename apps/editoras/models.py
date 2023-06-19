from django.db import models

class Editora(models.Model):
    nome = models.CharField('Nome', max_length=50)
    endereco = models.CharField('Endereço', max_length=200)
    #livros_publicados = models.ManyToManyField('Livro', verbose_name='Livros Publicados')

    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'
        ordering = ['id']

    def __str__(self):
        return self.nome
            