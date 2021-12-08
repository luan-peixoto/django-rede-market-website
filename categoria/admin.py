from django.contrib import admin

# Register your models here.

from .models import Categoria
# esses dois comandos fazem com que seja possível alterar a tabela categoria pela interface
# administrativa do django

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Categoria, CategoriaAdmin)