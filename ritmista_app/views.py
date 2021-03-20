from rest_framework import viewsets
from ritmista_app.models import *
from ritmista_app.serializer import *


class CursosViewset(viewsets.ModelViewSet):
    """Exibe todos os cursos cadastrados"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class GruposViewset(viewsets.ModelViewSet):
    """Exibe todos os grupos cadastrados"""
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

class NaipesViewset(viewsets.ModelViewSet):
    """Exibe todos os naipes cadastrados"""
    queryset = Naipe.objects.all()
    serializer_class = NaipeSerializer

class RitmistasViewset(viewsets.ModelViewSet):
    """Exibe todos os ritmistas cadastrados"""
    queryset = Ritmista.objects.all()
    serializer_class = RitmistaSerializer
