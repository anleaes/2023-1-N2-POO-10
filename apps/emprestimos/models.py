from django.db import models
from livros.models import Livro
from usuarios.models import Usuario

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name="livro", default=None)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="usuario", default=None)
    data_emprestimo = models.DateField('Data de Empréstimo')
    data_devolucao = models.DateField('Data de Devolução')

    class Meta:
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'
        ordering = ['id']

    def __str__(self):
        return f'{self.livro.titulo} emprestado por {self.usuario.nome}' 