from django.shortcuts import render, get_object_or_404
from receitas.models import Receita

def receitas(request):
    
    lista_receitas = Receita.objects.filter(categoria_id=1).order_by('id')
    return render(request, './paginas/receitas.html', {'receitas' : lista_receitas})
    # "./receitas.html" é o caminho do arquivo html a ser renderizado
    # por padrão o django procura os arquivos html em todas as pasta template que precisa
    # ser criada na raiz de cada app, porém caso seja adicionado 
    # os.path.join(BASE_DIR, 'templates') em settings.py, ele procura tambem em 
    # ./raiz/templates/algo , é preciso ter cuidado pois ele junta todas as pastas template em
    # uma só, se houver dois arquivos html com o mesmo nome em diferentes paginas template,
    # vai dar conflito

    # o dicionario a ser renderizado é chamado 'context' basicamente ele contem um conjunto de 
    # objetos que são passados para a página a ser renderizada

def receita(request, id, slug):
    receita = get_object_or_404(Receita, pk=id)
    # recupera a receita a ser exibida

    return render(request, 'paginas/receita.html', {'receita' : receita})
