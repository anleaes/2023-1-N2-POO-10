from django.db import models
#from emprestimos.models import Emprestimo

# Create your models here.

class Usuario(models.Model):
    name = models.CharField('Nome', max_length=50)
    address = models.TextField('Endereco', max_length=100) 
    #emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering =['id']

    def __str__(self):
        return self.name