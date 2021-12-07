from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=100, db_index=True, unique=True, default='titulo')
    slug = models.SlugField(max_length=100)

    imagem = models.CharField(max_length=50, blank=True)

    data = models.CharField(max_length=50, default="10/10/2020")

    desc_mini = models.CharField(max_length=300, blank=True)
    desc_full = models.CharField(max_length=5000, blank=True)
    


    likes = models.IntegerField(default=0)
    deslikes = models.IntegerField(default=0)

    class Meta: 
        # essa classe define os metadados da entidade categoria

        db_table = 'noticias'
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