from django.contrib import admin
from ritmista_app.models import Curso, Grupo, Naipe, Ritmista


class Grupos(admin.ModelAdmin):
    list_display = ('id', 'grupo')
    list_display_links = ('id', 'grupo')
    search_fields = ('grupo',)
    list_filter = ('grupo',)

admin.site.register(Grupo, Grupos)


class Naipes(admin.ModelAdmin):
    list_display = ('id', 'naipe')
    list_display_links = ('id', 'naipe')
    search_fields = ('naipe',)
    list_filter = ('naipe',)

admin.site.register(Naipe, Naipes)


class Cursos(admin.ModelAdmin):
    list_display = ('id', 'curso')
    list_display_links = ('id', 'curso')
    search_fields = ('curso',)
    list_filter = ('curso',)

admin.site.register(Curso, Cursos)


class Ritmistas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'curso', 'naipe', 'cpf', 'telefone')
    list_display_links = ('nome', 'naipe')
    search_fields = ('nome', 'naipe', 'curso')
    list_filter = ('naipe', 'data_entrada',)

admin.site.register(Ritmista, Ritmistas)
