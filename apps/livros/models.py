from django.db import models
from autor.models import Autor
from editoras.models import Editora
from categorias.models import Categoria

# Create your models here.

class Livro(models.Model):
    title = models.CharField('Titulo', max_length=50)
    isbn = models.CharField('ISBN', max_length=50) 
    available = models.BooleanField('Disponivel', default=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="autor", default=None)
    editoras = models.ForeignKey(Editora, on_delete=models.CASCADE, related_name="editoras", default=None)
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="categorias", default=None)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering =['id']

    def __str__(self):
        return self.title