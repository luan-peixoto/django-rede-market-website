from django import forms
from django.forms.widgets import TextInput
from receitas.models import Receita


class ReceitaIdForm(forms.Form):

    receita_id = forms.CharField(widget=forms.HiddenInput())
