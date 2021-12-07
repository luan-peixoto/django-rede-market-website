from django.db import models

# Create your models here.

class Categoria(models.Model):
    # quando você cria uma entidade e não define uma primary key, o django
    # automaticamente cria a primary key com nome 'id'

    nome = models.CharField(max_length=70, db_index=True, unique=True)
    # db_index = true faz com que o atributo 'nome' seja indexado, ou seja, ao fazer buscas
    # usando o nome, essas buscas são otimizadas e se tornam mais rápidas

    slug = models.SlugField(max_length=70) 
    # slug é uma parte do texto que vai aparecer na pagina html
    #  ex: produtos/produto-1, 'produto-1' é o slug
    
    class Meta: 
        # essa classe define os metadados da entidade categoria

        db_table = 'categoria'
        # faz com que o nome da tabela a ser criado passe a ser 'categoria', ao invés de
        # {nome_app}_{nome_classe}
        
        ordering = ('nome', 'slug',)
        #define a ordem que as tabelas vão aparecer no bd

    def __str__(self):
        return self.nome
    # ao realizar algum comando que transforme um objeto categoria em string, por exemplo
    # print(cat), o método acima faz com que ao invés de ser retornado algo como 
    # <objeto - nome: 'nome', slug: 'slug>, seja retornado apenas objeto.nome, que no caso
    # é o atributo nome do objeto em forma de string