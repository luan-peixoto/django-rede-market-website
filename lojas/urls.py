from django.urls import path
from lojas import views

app_name = "lojas"
# é preciso informar o nome do app com a variável app_name, depois colocá-lo no arquivo
# settings.py

urlpatterns = [
    path('lojas/', views.lojas, name="index"), 
    # o atributo name de um path serve para dizer qual é o nome a ser colocado caso queira [
    # criar um href="{% url 'app_nome:nome' %}"
]