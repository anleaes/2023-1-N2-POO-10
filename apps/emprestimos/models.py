from django.db import models

class Emprestimo(models.Model):
    livro = models.CharField('Livro', max_length=50)
    usuario = models.CharField('Usuário', max_length=50)
    data_emprestimo = models.DateField('Data de Empréstimo')
    data_devolucao = models.DateField('Data de Devolução')

    class Meta:
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'
        ordering = ['id']

    def __str__(self):
        return self.livro
       
       
#     podemos obter e definir os valores dos atributos da classe Emprestimo utilizando os seguintes metodos:
#     emprestimo = Emprestimo(livro, usuario, data_emprestimo, data_devolucao)
#     print(emprestimo.get_livro())  # Obtém o livro do empréstimo
#     emprestimo.set_data_devolucao(nova_data_devolucao)  # Define uma nova data de devolução
