from rest_framework import serializers
from cursos.models import Curso

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ("id", "nombre", "descripcion", "profesores", "alumnos")