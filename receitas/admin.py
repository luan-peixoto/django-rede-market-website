from django.contrib import admin

# Register your models here.

from .models import Receita
admin.site.register(Receita)
# esses dois comandos fazem com que seja possível alterar a tabela Receita pela interface
# administrativa do django