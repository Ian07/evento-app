from rest_framework import serializers
from cursos.models import Curso, Clase, Charla
from participantes.serializers import PersonaSerializer

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ("id", "nombre", "slogan", "descripcion", "profesores", "alumnos", "clases","imagen")

class ClaseSerializer(serializers.ModelSerializer):
    presentes = PersonaSerializer(many=True, read_only=True)
    class Meta:
        model = Clase
        fields = ("id", "dia", "hora_inicio", "hora_fin", "aula", "curso", "presentes")


class CharlaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charla
        fields = ("id", "dia", "hora_inicio", "hora_fin", "aula", "disertantes", "nombre", "descripcion")
        