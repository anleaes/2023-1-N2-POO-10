from django.db import models

# Create your models here.
#Criando a classe biblioteca
class Biblioteca(models.Model):
    #criando seu atibutos
    nome = models.CharField('Nome', max_length=50)
    endereco = models.TextField('Endereço')
    
    #relacionando atributos com Livro e Usuário (outras classes)
    
    livros = models.ForeignKey('Livro', on_delete=models.CASCADE, related_name='biblioteca')
    usuarios = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='biblioteca')
    
    #criando os métodos de adição e remoção de livro da biblioteca, atrelado a classe "Livro"
    
    def adicionarLivro(self, livro):
        self.livros.add(livro)
        
    def removerLivro(self, livro):
        self.livros.remove(livro)
        
    #criando os métodos de busca de livro
    
    def buscarLivroPorTitulo(self, titulo):
        livros_encontrados = []
        for livro in self.livros.all():
            if livro.titulo == titulo:
                livros_encontrados.append(livro)
        return livros_encontrados

    def buscarLivroPorAutor(self, autor):
        livros_encontrados = []
        for livro in self.livros.all():
            if livro.autor.nome == autor:
                livros_encontrados.append(livro)
        return livros_encontrados

    #criando o método de mostrar disponibilidade
    
    def listarLivrosDisponiveis(self):
        livros_disponiveis = []
        for livro in self.livros.all():
            if not Emprestimo.objects.filter(livro=livro).exists():
                livros_disponiveis.append(livro)
        return livros_disponiveis

    #criando os métodos de registro de usuário, atrelado a classe 'Usuario'
    
    def adicionarUsuario(self, usuario):
        self.usuarios.add(usuario)

    def removerUsuario(self, usuario):
        self.usuarios.remove(usuario)
    
    def __str__(self):
        return self.nome