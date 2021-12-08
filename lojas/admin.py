from django.contrib import admin

# Register your models here.

from .models import Loja
# esses dois comandos fazem com que seja possível alterar a tabela Loja pela interface
# administrativa do django

class LojaAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Loja, LojaAdmin)