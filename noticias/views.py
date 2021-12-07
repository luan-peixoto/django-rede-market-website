from django.shortcuts import render
from django.core.paginator import Paginator

from noticias.models import Noticia

def noticias(request):
    lista_noticias = Noticia.objects.all().order_by('id')
    paginator = Paginator(lista_noticias, 4) 
    # o atributo paginator faz a paginação dos objetos de lista_noticias e define um limite
    # de 4 objetos por página
    pagina_atual = request.GET.get('pagina')
    # request.GET.get('pagina') pede um atributo chamado 'pagina' que deve estar no url do site
    # no caso seria algo tipo '?pagina=X', 
    # atributo pagina_atual recebe 'none' ao acessar a página diretamente pelo link 'noticias' 
    # da navbar, pois não existe nenhum atributo página no url, ele 'pages/noticias/'

    # ao clicar em algum href dentro do paginator do arquivo noticias.html, o usuário é 
    # redirecionado para 'pages/noticias/?pagina=x', isso recarrega a view e faz com 
    # que o atributo pagina atual passe a ter o valor de 'x'


    page_obj_noticias = paginator.get_page(pagina_atual)
    # pega uma das páginas do atributo paginator, como a variável página é 'none' ao ser 
    # acessada por algum link noticias ('pages/noticias/'), o objeto retornado será o conjunto
    # de objetos da página 1

    # caso seja acessado por algum link 'pages/noticias/?pagina=x', o objeto retornado será
    # o conjunto de objetos da página x

    return render(request, './paginas/noticias.html', {'noticias' : page_obj_noticias})
    # "./noticias.html" é o caminho do arquivo html a ser renderizado
    # por padrão o django procura os arquivos html em todas as pasta template que precisa
    # ser criada na raiz de cada app, porém caso seja adicionado 
    # os.path.join(BASE_DIR, 'templates') em settings.py, ele procura tambem em 
    # ./raiz/templates/algo , é preciso ter cuidado pois ele junta todas as pastas template em
    # uma só, se houver dois arquivos html com o mesmo nome em diferentes paginas template,
    # vai dar conflito

    # o dicionario a ser renderizado é chamado 'context' basicamente ele contem um conjunto de 
    # objetos que são passados para a página a ser renderizada


    
def cadastrar_noticia(request):


    page = []

    return render(request, './paginas/cadastrar_noticia.html', {'noticias' : page})