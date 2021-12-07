from django.db import models

from categoria.models import Categoria

class Receita(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='receitas', 
    on_delete= models.DO_NOTHING)
    # quando voce referencia uma foreign key, ela pega a primary key de outra entidade
    # e nomeia como {atributo}_{chave}, no caso como a primary key de categoria é a primary
    # key 'id' gerada automaticamente, o atributo categoria, passa a ser categoria_id

    # tendo um objeto de categoria, é possivel usar o comando, obj.receita_set.all() que
    # retorna todos os objetos de produto com a categoria em questão, porém o atributo
    # related_name='receitas' faz com que seja possível simplificar esse comando, digitando
    # apenas obj.receitas.all()

    titulo = models.CharField(max_length=100, db_index=True, default='titulo')
    imagem = models.CharField(max_length=50, blank=True)

    slug = models.SlugField(max_length=100)

    tempo = models.CharField(max_length=50, blank=True)
    rendimento = models.CharField(max_length=50, blank=True)
    dificuldade = models.CharField(max_length=50, blank=True)
    modo_servir = models.CharField(max_length=50, blank=True)
    
    ingredientes = models.CharField(max_length=500, blank=True)
    modo_preparo = models.CharField(max_length=1000, blank=True)

    likes = models.IntegerField(default=0)
    deslikes = models.IntegerField(default=0)

    class Meta: 
        # essa classe define os metadados da entidade categoria

        db_table = 'receitas'
        # faz com que o nome da tabela a ser criado passe a ser 'categoria', ao invés de
        # {nome_app}_{nome_classe}
        
        ordering = ('titulo',)
        #define a ordem que as tabelas vão aparecer no bd

    def __str__(self):
        return self.titulo
    # ao realizar algum comando que transforme um objeto categoria em string, por exemplo
    # print(cat), o método acima faz com que ao invés de ser retornado algo como 
    # <objeto - nome: 'nome', slug: 'slug>, seja retornado apenas objeto.nome, que no caso
    # é o atributo nome do objeto em forma de string