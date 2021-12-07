from django.db import models

class Loja(models.Model):
    nome = models.CharField(max_length=100, db_index=True, unique=True, default='titulo')
    slug = models.SlugField(max_length=100)

    cidade = models.CharField(max_length=50, blank=True)
    bairro = models.CharField(max_length=50, blank=True)
    endereco = models.CharField(max_length=100, blank=True)

    telefone = models.CharField(max_length=15, blank=True)

    horario_sem = models.CharField(max_length=50, default= "07h as 22h")
    horario_fds = models.CharField(max_length=50, default= "07h as 20h")
 
    imagem = models.CharField(max_length=50, blank=True)

    class Meta: 
        # essa classe define os metadados da entidade categoria

        db_table = 'lojas'
        # faz com que o nome da tabela a ser criado passe a ser 'categoria', ao invés de
        # {nome_app}_{nome_classe}
        
        ordering = ('nome',)
        #define a ordem que as tabelas vão aparecer no bd

    def __str__(self):
        return self.nome
    # ao realizar algum comando que transforme um objeto categoria em string, por exemplo
    # print(cat), o método acima faz com que ao invés de ser retornado algo como 
    # <objeto - nome: 'nome', slug: 'slug>, seja retornado apenas objeto.nome, que no caso
    # é o atributo nome do objeto em forma de string