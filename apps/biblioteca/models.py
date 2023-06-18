from django.db import models
# from django_extensions.db.fields import OneToManyField

# Create your models here.
#Criando a classe biblioteca
class Biblioteca(models.Model):
    #criando seu atibutos
    nome = models.CharField('Nome', max_length=50)
    endereco = models.TextField('Endereço')
    
    #relacionando atributos com Livro e Usuário (outras classes)
    
    #livros = OneToManyField('Livro', related_name='biblioteca')
    #usuarios = OneToManyField('Usuario', related_name='biblioteca')
    
    #criando os métodos de adição e remoção de livro da biblioteca, atrelado a classe "Livro"
    
    #def adicionarLivro(self, livro):
        #self.livros.add(livro)
        
  #  def removerLivro(self, livro):
      #  self.livros.remove(livro)
        
    #criando os métodos de busca de livro
    
 #   def buscarLivroPorTitulo(self, titulo):
    #    return self.livros.filter(titulo__icontains=titulo)

  #  def buscarLivroPorAutor(self, autor):
   #     return self.livros.filter(autor__icontains=autor)

    #criando o método de mostrar disponibilidade
    
  #  def listarLivrosDisponiveis(self):
    #    return self.livros.exclude(emprestimo__isnull=False)

    #criando os métodos de registro de usuário, atrelado a classe 'Usuario'
    
  #  def adicionarUsuario(self, usuario):
   #     self.usuarios.add(usuario)

 #   def removerUsuario(self, usuario):
   #     self.usuarios.remove(usuario)
    
  #  def __str__(self):
     #   return self.nome