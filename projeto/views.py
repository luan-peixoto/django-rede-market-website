from django.shortcuts import render
from receitas.models import Receita
from noticias.models import Noticia

def index(request):
    lista_noticias = Noticia.objects.all().order_by('id')[:6]
    lista_receitas = Receita.objects.filter(categoria_id=1).order_by('id')[:3]
    return render(request, './index.html', {'noticias' : lista_noticias[:6], 'receitas' : lista_receitas[:3]})
    # "./index.html" é o caminho do arquivo html a ser renderizado
    # por padrão o django procura os arquivos html em todas as pasta template que precisa
    # ser criada na raiz de cada app, porém caso seja adicionado 
    # os.path.join(BASE_DIR, 'templates') em settings.py, ele procura tambem em 
    # ./raiz/templates/algo , é preciso ter cuidado pois ele junta todas as pastas template em
    # uma só, se houver dois arquivos html com o mesmo nome em diferentes paginas template,
    # vai dar conflito

    # o dicionario a ser renderizado é chamado 'context' basicamente ele contem um conjunto de 
    # objetos que são passados para a página a ser renderizada


def quem_somos(request):
    lista = ['a', 'b', 'c']
    return render(request, './paginas/quem-somos.html', {'lista' : lista})

def contato(request):
    lista = ['a', 'b', 'c', '4']
    return render(request, './paginas/contato.html', {'lista' : lista})