from django.contrib import admin

# Register your models here.

from .models import Categoria
admin.site.register(Categoria)
# esses dois comandos fazem com que seja possível alterar a tabela categoria pela interface
# administrativa do django