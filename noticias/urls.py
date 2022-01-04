from django.urls import path
from noticias import views

app_name = "noticias"
# é preciso informar o nome do app com a variável app_name, depois colocá-lo no arquivo
# settings.py de projeto

urlpatterns = [
    path('noticias/', views.noticias, name="index"), 
    # o atributo name de um path serve para dizer qual é o nome a ser colocado caso queira [
    # criar um href="{% url 'app_nome:nome' %}"

    path('noticias/<int:id>/<slug:slug>/', views.noticia, name="noticia"), 

    path('listar_noticias/', views.listar_noticias, name="listar-noticias"), 

    path('backup_listar_noticias/', views.backup_listar_noticias, name="backup-listar-noticias"),

    path('criar_editar_noticia/', views.criar_editar_noticia, name="criar-editar-noticia"),  
    
    path('detalhes_noticia/<int:id>/<slug:slug>/', views.detalhes_noticia, name="detalhes-noticia"), 

    path('editar_noticia/<int:id>/<slug:slug>/', views.editar_noticia, name="editar-noticia"),

    
    path('remover_noticia/', views.remover_noticia, name="remover-noticia"),  


]