from django.contrib import admin

from .models import Precos

# Register your models here.


class PrecosAdmin(admin.ModelAdmin):
    list_display = ("preco", "moeda",  "data")
    list_display_links = ("preco", "moeda", "data")
    # adiciona filtro area administrativa Contatos

    # limita a quantidade de contatos por pagina
    list_per_page = 50

    # Insere campos de pesquisa
    search_fields = ("moeda", "data")

    # Permite a edição sem precisar entrar em detalhes
    list_editable = ("moeda", "preco", "data")

admin.site.register(Precos)
