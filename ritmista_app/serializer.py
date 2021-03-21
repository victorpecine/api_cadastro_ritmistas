from rest_framework import serializers
from ritmista_app.models import Curso, Grupo, Naipe, Ritmista


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'


class NaipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Naipe
        fields = '__all__'


class RitmistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ritmista
        fields = '__all__'


class ListaRitmistasNaipeSerializer(serializers.ModelSerializer):
    # traz na tela o nome do curso com base no id
    curso = serializers.ReadOnlyField(source='curso.curso')

    class Meta:
        model = Ritmista
        fields = ['nome', 'curso']
