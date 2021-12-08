from django.contrib import admin

# Register your models here.

from .models import Receita
# esses dois comandos fazem com que seja possível alterar a tabela Receita pela interface
# administrativa do django

class ReceitaAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Receita, ReceitaAdmin)