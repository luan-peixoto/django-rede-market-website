from django.contrib import admin

# Register your models here.

from .models import Noticia
# esses dois comandos fazem com que seja possível alterar a tabela Noticia pela interface
# administrativa do django

class NoticiaAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Noticia, NoticiaAdmin)