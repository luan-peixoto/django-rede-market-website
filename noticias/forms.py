from django import forms
from django.forms.widgets import TextInput
from noticias.models import Noticia
from projeto import settings
from django.core.validators import RegexValidator

# 
class PesquisaNoticiaForm(forms.Form):
    # forms.Form é a classe usada quando é preciso criar um formulário que não use nenhum 
    # modelo para nada, caso o form tenha relação com algum modelo, a classe deve ser 
    # forms.ModelForm

    titulo = forms.CharField(
        widget = TextInput(attrs=({'class' : 'form-control form-control-sm', 
        'maxlenght' : '100'})),
        required = False,
    )
    # titulo é um elemento html de form input criado pelo django, feito para substituir o 
    # elemento <input type='text' name='titulo' id='id_titulo' class='form-control form-control-sm' 
    # maxlength='100'>
                  
    # Charfield diz que é um campo de texto, ou seja, qualquer caracter pode ser digitado nele
    # TextInput define que é um elemento tipo <input> com a propriedade type='text'

    # attrs="" são as propriedades extras que queremos adicionar

    # required = False diz que o campo não é de preenchimento obrigatório


class CriarEditarNoticiaForm(forms.ModelForm):
    # como o formulário de cadastro de notícia vai ser feito com base num modelo, no caso
    # o modelo 'Noticia' que cria objetos notícia para salvar no bd, é necessário adicionar
    # 'forms.ModelForm' como parâmetro
    class Meta:
        model = Noticia
        # usa como modelo a classe 'Noticia', ou seja, cada campo dela vai ser tornar um campo
        # do form por padrão
        fields = {'titulo', 'imagem', 'data', 'desc_mini', 'desc_full'}
        # define quais campos realmente entraram para o form, se o atributo 'fields' não exisiti
        # sse, todos os campos da classe 'Noticia' entrariam

    titulo = forms.CharField(
        error_messages = {'required': 'Campo obrigatório!', 'unique': 'Título duplicado!'},
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Título', 'class': 'form-control form-2', 'max-lenght': '100'
            }
        )
    )

    # forms.TextInput gera um elemento do tipo input, o nome do atributo 'titulo faz com que
    # name="titulo" e id="id_titulo", esse código gera o seguinte elemento:
    # <input class="form-control form-2" type="text" name="titulo" maxlength="100" required="" id="id_titulo" placeholder="Título">
                        

    data = forms.DateField(
        error_messages = {'required': 'Campo obrigatório!', 'invalid': 'Data inválida!'},
        input_formats = settings.DATE_INPUT_FORMATS,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Data (dd/mm/yyyy)', 'class': 'form-control form-2'
            }
        )
    )

    # <input class="form-control form-2" type="text" name="data" required="" id="id_data" placeholder="Data (dd/mm/yyyy)">
                
    imagem = forms.CharField(
        error_messages = {'required' : 'Campo obrigatório!'},
        validators = [RegexValidator(regex='^[a-z-0-9_]+\.(jpg|png|gif|bmp)$', message="Url de imagem inválido.")],
        widget=forms.TextInput(
            attrs = {
                'placeholder': 'Imagem (nome.extensão)', 'class': 'form-control form-2', 'max-lenght': '50'
            }
        )
    )

    # <input class="form-control form-2" type="text" name="imagem" maxlength="50" required="" id="id_imagem" placeholder="Imagem (nome.extensão)">
               
    desc_mini = forms.CharField(
        error_messages = {'required': 'Campo obrigatório!'},
        widget = forms.Textarea(
            attrs = {
                'placeholder': 'Descrição breve', 'class': 'form-control form-2', 'max-lenght': '300',
                'rows': '8'
            }
        )
    )

    # <textarea class="form-control form-2"  type="text" name="desc_mini" maxlength="300" required="" id="id_desc_mini" placeholder="Descrição breve" rows="8"></textarea>

    desc_full = forms.CharField(
        error_messages = {'required': 'Campo obrigatório!'},
        widget = forms.Textarea(
            attrs = {
                'placeholder': 'Descrição completa', 'class': 'form-control form-2', 'max-lenght': '5000',
                'rows': '18'
            }
        )
    )

    # <textarea class="form-control form-2"  type="text" name="desc_full" maxlength="5000" required="" id="id_desc_full" placeholder="Descrição completa" rows="18"></textarea>