from django.contrib import admin

# Register your models here.

from .models import Noticia
admin.site.register(Noticia)
# esses dois comandos fazem com que seja possível alterar a tabela Noticia pela interface
# administrativa do django