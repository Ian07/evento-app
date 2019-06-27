from rest_framework import serializers
from participantes.models import Persona, Alumno, Profesor, Disertante, Organizador, Usuario
from api_eventos import settings
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.six import text_type

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ("documento", "nombre", "apellido")

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ("id", "TIPO", "ROLNAME", "persona",)

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ("id", "TIPO", "ROLNAME", "persona")

class DisertanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disertante
        fields = ("id", "TIPO", "ROLNAME", "persona")

class OrganizadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizador
        fields = ("id", "TIPO", "ROLNAME", "persona")

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ("id", "TIPO", "ROLNAME", "persona", "username")

class UsuarioSerializerconToken(serializers.ModelSerializer):
    """
    Se utiliza para registrarse, momentaneamente solo va crear el usuario,
    no lo va asociar a la persona, esto es solo para fines de probar la
    relación entre la API y React.

    Para más información consultar:
    https://medium.com/@dakota.lillie/django-react-jwt-authentication-5015ee00ef9a
    """

    token = serializers.SerializerMethodField()

    def get_token(self, user):
        tokens = RefreshToken.for_user(user)
        refresh = text_type(tokens)
        access = text_type(tokens.access_token)
        data = {
            "refresh": refresh,
            "access": access
        }
        return data

    class Meta:
        model = Usuario
        fields = ('token', 'username', 'email')