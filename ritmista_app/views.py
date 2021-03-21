from rest_framework import viewsets, generics
from ritmista_app.models import Curso, Grupo, Naipe, Ritmista
from ritmista_app.serializer import CursoSerializer, GrupoSerializer, NaipeSerializer, RitmistaSerializer, ListaRitmistasNaipeSerializer


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


class ListaRitmistasNaipe(generics.ListAPIView):
    def get_queryset(self):
        # filtrando os ritmistas pelo id do naipe
        queryset = Ritmista.objects.filter(naipe=self.kwargs['pk'])
        return queryset
    serializer_class = ListaRitmistasNaipeSerializer
