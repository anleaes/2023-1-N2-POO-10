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
            
    
    
    
    # usando métodos getter e setter para obter e definir os valores dos atributos da classe Editora, 
    # exemplo a seguir:

#    editora = Editora("Nome da Editora", "Endereço da Editora")
#    print(editora.get_nome())  # Obtém o nome da editora
#    editora.set_endereco("Novo Endereço")  # Define um novo endereço para a editora


    # com a classe livro ja feita pode usar 
    # a classe Editora para adicionar, remover e listar os livros publicados pela editora, 
    # exemplo a seguir:
    
#   editora = Editora("Nome da Editora", "Endereço da Editora")

#   livro1 = Livro("Título 1", "Autor 1")
#   livro2 = Livro("Título 2", "Autor 2")

#   editora.adicionar_livro_publicado(livro1)
#   editora.adicionar_livro_publicado(livro2)

#   editora.listar_livros_publicados()

#   editora.remover_livro_publicado(livro1)

#   editora.listar_livros_publicados()
