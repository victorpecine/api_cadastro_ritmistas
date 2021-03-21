from rest_framework import viewsets, generics
from ritmista_app.models import Curso, Grupo, Naipe, Ritmista
from ritmista_app.serializer import (CursoSerializer, GrupoSerializer, NaipeSerializer,
                                     RitmistaSerializer, ListaRitmistasNaipeSerializer)
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class CursosViewset(viewsets.ModelViewSet):
    """Exibe todos os cursos cadastrados"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    # exige autenticação com login e senha para acesso
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class GruposViewset(viewsets.ModelViewSet):
    """Exibe todos os grupos cadastrados"""
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class NaipesViewset(viewsets.ModelViewSet):
    """Exibe todos os naipes cadastrados"""
    queryset = Naipe.objects.all()
    serializer_class = NaipeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class RitmistasViewset(viewsets.ModelViewSet):
    """Exibe todos os ritmistas cadastrados"""
    queryset = Ritmista.objects.all()
    serializer_class = RitmistaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaRitmistasNaipe(generics.ListAPIView):
    def get_queryset(self):
        # filtrando os ritmistas pelo id do naipe
        queryset = Ritmista.objects.filter(naipe=self.kwargs['pk'])
        return queryset
    serializer_class = ListaRitmistasNaipeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
