from django.shortcuts import render
from receitas.models import Receita
from noticias.models import Noticia
from noticias.forms import NoticiaIdForm
from receitas.forms import ReceitaIdForm

def index(request):
    lista_noticias = Noticia.objects.all().order_by('id')[:6]
    lista_receitas = Receita.objects.order_by('id')[:3]

    lista_de_forms_id_noticia = []
    for noticia in lista_noticias:
        lista_de_forms_id_noticia.append(NoticiaIdForm(initial= {'noticia_id': noticia.id}))
        # cria um formulário de quantidade e id para cada noticia

    lista_de_forms_id_receita = []
    for receita in lista_receitas:
        lista_de_forms_id_receita.append(ReceitaIdForm(initial= {'receita_id': receita.id}))
        # cria um formulário de quantidade e id para cada receita

    return render(request, './index.html', {'noticias' : zip(lista_noticias, lista_de_forms_id_noticia), 'receitas' : zip(lista_receitas, lista_de_forms_id_receita)})
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