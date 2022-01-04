from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from noticias.models import Noticia
from noticias.forms import PesquisaNoticiaForm, CriarEditarNoticiaForm
from django.template.defaultfilters import slugify

from django.contrib import messages

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

def noticia(request, id, slug):
    noticia = get_object_or_404(Noticia, pk=id)
    # recupera a notícia a ser exibida

    return render(request, 'paginas/noticia.html', {'noticia' : noticia})

    
def listar_noticias(request):
    form_pesquisa = PesquisaNoticiaForm(request.GET)
    # esse get pega o atributo com valor ?titulo= porque foi definido assim no form
    # quando é enviado para a pagina html ele faz o mesmo, mas ao inves disso ele dá
    # submit em ?titulo="algumtexto"
    # instancia um objeto de formulario e envia como objeto para o html, tambem
    # pega no browser a pesquisa enviada por esse objeto, caso a pagina seja acessada 
    # diretamente, pega ""

    if form_pesquisa.is_valid():
        # caso nenhuma regra de input do form esteja sendo violada
        titulo = form_pesquisa.cleaned_data['titulo']

        lista_noticias = Noticia.objects.all().filter(titulo__icontains=titulo).order_by('id')
        # '.filter(titulo__icontains=titulo)' filtra apenas os objetos que contenham o texto
        # do form no atributo titulo

        obj_per_page = 4
        paginator = Paginator(lista_noticias, obj_per_page)
        pagina_atual = request.GET.get('pagina')
        page_obj_noticias = paginator.get_page(pagina_atual)

        n = 0
        if lista_noticias.count() < obj_per_page:
            n = range(obj_per_page - lista_noticias.count())
        else:
            if lista_noticias.count() % obj_per_page != 0:
                n = range(obj_per_page - (lista_noticias.count() % obj_per_page))
            else:
                n = range(0)
        # quantidade de tabelas que não foram carregadas

        return render(request, './paginas/listar_noticias.html', {'noticias' : page_obj_noticias, 
        'n' : n, 'form_pesquisa' : form_pesquisa})
    else:
        raise ValueError("ERRO DE VALIDAÇÃO - FORMULÁRIO INVÁLIDO")


def backup_listar_noticias(request):
    lista_noticias = Noticia.objects.all().order_by('id')
    obj_per_page = 4
    paginator = Paginator(lista_noticias, obj_per_page)
    pagina_atual = request.GET.get('pagina')
    page_obj_noticias = paginator.get_page(pagina_atual)

    n = range(int(lista_noticias.count() % obj_per_page))
    # quantidade de tabelas que não foram carregadas
    
    return render(request, './paginas/backup_listar_noticias.html', {'noticias' : page_obj_noticias, 'n' : n})


def criar_editar_noticia(request):
    # caso um request seja enviado, a view é recarregada e ele fica salvo no parametro 'request'

    if request.POST:
        # caso o request seja do tipo post


        noticia_id = request.session.get('noticia_id')
        # tenta recuperar o id da noticia armazenado no cookie de sessão

        if noticia_id:
            # caso seja encontrado, trata-se de uma edição de notícia

            noticia = get_object_or_404(Noticia, pk=noticia_id)
            # recupera a notícia a ser alterada
            formulario_noticia = CriarEditarNoticiaForm(request.POST, instance=noticia)
            # cria um formulário usando os dados que estão na notícia
        else:
            # caso contrário, trata-se de uma criação de notícia

            formulario_noticia = CriarEditarNoticiaForm(request.POST)
            # cria uma instância de um formulário contendo os dados enviados no request 'POST'

        if formulario_noticia.is_valid():
            # caso o formulário postado seja válido

            noticia = formulario_noticia.save(commit=False)
            # cria uma instância de Notícia para colocar no bd, mas não envia
            noticia.slug = slugify(noticia.titulo)
            # adiciona um slug à notícia usando o título como base
            noticia.save()
            # salva ou atualiza a notícia no banco de dados

            if noticia_id:
                # caso seja uma edição
                messages.add_message(request, messages.INFO, 'Notícia alterada com Sucesso!')
                # adiciona uma mensagem de sucesso podera ser usada apenas dentro da view atual
                del request.session['noticia_id']
                # remove do cookie de sessão o id da notícia que foi alterada
            else:
                messages.add_message(request, messages.INFO, 'Notícia adicionada com Sucesso!')
                # adiciona uma mensagem de sucesso podera ser usada apenas dentro da view atual
            
            """
            return render(request, './paginas/detalhes_noticia.html', {'noticia': noticia})
            """
            # quando o servidor retorna atráves de render uma página qualquer, caso o usuário
            # atualize a página, o formulário da notícia será adicionado novamente no bd
            # por isso, não deve-se usar o render, e sim o redirect:

            return redirect('noticias:detalhes-noticia', id = noticia.id, slug = noticia.slug)
            # o slug passado aqui não será usado para nada, o importante é o parametro 'id' que
            # vai definir qual noticia será passada para a view 'detalhes_noticia'


    else:
        if 'noticia_id' in request.session:
            # isso impede que ao clicar em editar noticia e depois cadastrar noticia, a página
            # de cadastro crie uma edição, isso poderia ser evitado também separando a parte de
            # edição e colocando na view editar_noticia
            del request.session['noticia_id']

        formulario_noticia = CriarEditarNoticiaForm()
        # cria uma instância de um formulário vazio definido pela classe CriarEditarNoticiaForm()
        
    return render(request, './paginas/criar_editar_noticia.html', {'form': formulario_noticia})


def detalhes_noticia(request, id, slug):
    noticia = get_object_or_404(Noticia, pk=id)
    # recupera a notícia a ser exibida baseado no id recebido como parametro

    request.session['noticia_id_del'] = id
    # cria uma sessão de noticia a ser deletada caso seja necessário

    return render(request, './paginas/detalhes_noticia.html', {'noticia': noticia})


def editar_noticia(request, id, slug):
    # essa view (ou url) só pode ser acessada pela view detalhes_noticia, ela possui um botão 
    # editar que leva pra esta view e envia o id e slug da notícia a ser editada

    noticia = get_object_or_404(Noticia, pk=id)
    # recupera o objeto notícia do bd com o id recebido de parâmetro

    noticia_form = CriarEditarNoticiaForm(instance=noticia)
    # gera um formulário de notícia com os dados pré-definidos no objeto noticia recuperado

    request.session['noticia_id'] = id
    # como no formulário não existe o parametro id, pois ele é gerado automaticamente pelo 
    # django e como ele não vai ser adicionado, já que é perigoso definir esse campo, é 
    # necessário passar o id de outra forma, no caso criando um cookie de sessão com o id, que 
    # fica armazenado no servidor e expira após determinado tempo.
    # essa é a forma mais segura de passar o id de um objeto, definir uma variável 'id' e passar
    # para o dicionário também não é recomendado.

    return render(request, './paginas/criar_editar_noticia.html', {'form' : noticia_form, 'noticia': noticia.titulo})
    # renderiza o template criar_editar_noticia.html na view (url) edita_produto

def remover_noticia(request):
    noticia_id = request.session.get('noticia_id_del')
    # pega o id da noticia a ser deletado na sessão criada da view 'detalhes_noticia"

    noticia = get_object_or_404(Noticia, pk=noticia_id)
    # recupera do bd um objeto noticia com o id recebido
    noticia.delete()

    messages.add_message(request, messages.INFO, 'Notícia Removida com Sucesso!')
    
    return render(request, './paginas/detalhes_noticia.html', {'noticia' : noticia})
