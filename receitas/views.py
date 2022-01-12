from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from receitas.models import Receita
from receitas.forms import ReceitaIdForm

def receitas(request):
    
    lista_receitas = Receita.objects.order_by('id')

    lista_de_forms_id_receita = []
    for receita in lista_receitas:
        lista_de_forms_id_receita.append(ReceitaIdForm(initial= {'receita_id': receita.id}))
        # cria um formulário de quantidade e id para cada receita



    return render(request, './paginas/receitas.html', {'receitas' : zip(lista_receitas, lista_de_forms_id_receita)})
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
    receita_form = ReceitaIdForm(initial= {'receita_id': receita.id})

    return render(request, 'paginas/receita.html', {'receita' : receita, 'receita_form': receita_form})

def alterar_like_receita(request):
    if request.POST:
        # caso seja um request post
        id = request.POST.get("id")
        like = int(request.POST.get("like"))
        dislike = int(request.POST.get("dislike"))
        receita = get_object_or_404(Receita, pk=id)
        receita.likes = receita.likes + like
        receita.deslikes = receita.deslikes + dislike
        receita.save()
        # altera os likes da noticia

    return HttpResponse('')

def exibir_receitas_por_categoria(request):
    if request.POST:
        
        cat = request.POST.get("categoria")
        # recupera do request a categoria desejada
        if cat != '1':
            lista_receitas = Receita.objects.filter(categoria__id=cat).order_by('id')
        else:
            lista_receitas = Receita.objects.order_by('id')

        lista_de_forms_id_receita = []
        for receita in lista_receitas:
            lista_de_forms_id_receita.append(ReceitaIdForm(initial= {'receita_id': receita.id}))
            # cria um formulário de quantidade e id para cada receita

        return render(request, 'paginas/receitas_por_categoria.html', {'receitas' : zip(lista_receitas, lista_de_forms_id_receita)})
