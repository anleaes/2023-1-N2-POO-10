from django.db import models

# Create your models here.
#Criando a classe

class Categoria(models.Model):
    #adicionando seus atributos
    nome = models.CharField('Nome', max_length=200)
    descricao = models.TextField('Descricao')
    
    #Criando a classe meta
        
    class Meta:
            verbose_name_plural = "Categorias"


    def __str__(self):
        return self.nome