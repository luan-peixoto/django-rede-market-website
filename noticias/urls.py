from django.urls import path
from noticias import views

app_name = "noticias"
# é preciso informar o nome do app com a variável app_name, depois colocá-lo no arquivo
# settings.py de projeto

urlpatterns = [
    path('noticias/', views.noticias, name="index"), 
    # o atributo name de um path serve para dizer qual é o nome a ser colocado caso queira [
    # criar um href="{% url 'app_nome:nome' %}"
    path('cadastrar_noticia/', views.cadastrar_noticia, name="cadastrar-noticia"), 
]