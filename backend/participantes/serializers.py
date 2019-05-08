from rest_framework import serializers
from participantes.models import Persona, Profesor, Rol

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ("documento", "nombre", "apellido")


class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ("TIPO", "ROLNAME", "persona")
