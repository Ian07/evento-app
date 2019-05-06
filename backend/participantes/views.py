from rest_framework import generics
from participantes.models import Persona
from participantes.serializers import PersonaSerializer
from rest_framework.permissions import IsAuthenticated


class ListPersonasView(generics.ListAPIView):
    """
    Solamente da un manejador de GET
    """
    permission_classes = (IsAuthenticated,)

    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


