from django.contrib import admin
from .models import Categoria, Padaria, Produto, Cesta, Endereco

admin.site.register(Categoria)
admin.site.register(Padaria)
admin.site.register(Produto)
admin.site.register(Cesta)
admin.site.register(Endereco)
