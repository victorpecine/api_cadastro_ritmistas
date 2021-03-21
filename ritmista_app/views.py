from rest_framework import viewsets, generics
from ritmista_app.models import Curso, Grupo, Naipe, Ritmista
from ritmista_app.serializer import (CursoSerializer, GrupoSerializer, NaipeSerializer,
                                     RitmistaSerializer, ListaRitmistasNaipeSerializer)
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
import csv
from django.http import HttpResponse
from datetime import datetime


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


def exporta_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=ritmistas.csv'
    # encode UTF-8 no csv
    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    # nome das colunas no csv
    writer.writerow(['NOME', 'CURSO', 'NAIPE', 'GRUPO',
                     'DATA DE NASCIMENTO', 'CPF', 'TELEFONE',
                     'DATA DE ENTRADA', 'DATA DE SAÍDA'])

    ritmistas = Ritmista.objects.all().values_list('nome', 'curso', 'naipe', 'grupo',
                                                   'data_nascimento', 'cpf', 'telefone',
                                                   'data_entrada', 'data_saida')

    for ritmista in ritmistas:
        writer.writerow(ritmista)

    return response
