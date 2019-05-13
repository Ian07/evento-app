from rest_framework import serializers
from participantes.models import Persona, Alumno, Profesor, Disertante, Organizador

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ("documento", "nombre", "apellido")


class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ("TIPO", "ROLNAME", "persona",)


class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ("TIPO", "ROLNAME", "persona")


class DisertanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disertante
        fields = ("TIPO", "ROLNAME", "persona")


class OrganizadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizador
        fields = ("TIPO", "ROLNAME", "persona")

