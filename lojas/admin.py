from django.contrib import admin

# Register your models here.

from .models import Loja
admin.site.register(Loja)
# esses dois comandos fazem com que seja possível alterar a tabela Loja pela interface
# administrativa do django