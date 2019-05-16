from rest_framework import serializers
from cursos.models import Curso, Clase, Charla

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ("id", "nombre", "descripcion", "profesores", "alumnos", "clases")

class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ("id", "dia", "hora_inicio", "hora_fin", "aula", "curso", "presentes")


class CharlaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charla
        fields = ("id", "dia", "hora_inicio", "hora_fin", "aula", "disertantes", "nombre", "descripcion")
        