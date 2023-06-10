from django.db import models

# Create your models here.
class Autor(models.Model):
    name = models.CharField('Nome', max_length=50)
    nacionality = models.TextField('Nacionalidade', max_length=100)
    published_books = models.ForeignKey(Livro, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering =['id']

    def __str__(self):
        return self.name