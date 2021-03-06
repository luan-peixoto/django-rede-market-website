from django.urls import path
from receitas import views

app_name = "receitas"
# é preciso informar o nome do app com a variável app_name, depois colocá-lo no arquivo
# settings.py de projeto

urlpatterns = [
    path('receitas/', views.receitas, name="index"), 
    # o atributo name de um path serve para dizer qual é o nome a ser colocado caso queira [
    # criar um href="{% url 'app_nome:nome' %}"
    
    path('receitas/<int:id>/<slug:slug>/', views.receita, name="receita"),
    # url para mostrar a receita na página de receita 

    path('alterar_like_receita/', views.alterar_like_receita, name="alterar-like-receita"),  

    
    path('exibir_receitas_por_categoria/', views.exibir_receitas_por_categoria, name="exibir-receitas-por-categoria"),  

]