from django import forms
from django.forms.widgets import TextInput

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