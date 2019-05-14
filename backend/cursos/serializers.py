from rest_framework import serializers
from cursos.models import Curso, Clase

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ("id", "nombre", "descripcion", "profesores", "alumnos")


class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ("id", "dia", "hora_inicio", "hora_fin", "aula", "curso", "presentes")