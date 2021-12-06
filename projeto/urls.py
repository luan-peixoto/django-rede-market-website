from django.contrib import admin
from django.urls import path, include
from projeto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"), 
    # o atributo name de um path serve para dizer qual é o nome a ser colocado caso queira [
    # criar um href="{% url 'app_nome:nome' %}"
    
    path('quem-somos/', views.quem_somos, name="quem-somos"),
    path('pages/', include('noticias.urls')), 
    # faz com que eu possa incluir urls do app noticias com o endereco 'noticias/nome_app' 
    # nessa pagina, ou em qualquer href que esteja dentro de algum arquivo html da pagina
    path('pages/', include('receitas.urls')), 
    path('pages/', include('lojas.urls')), 

]

"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
