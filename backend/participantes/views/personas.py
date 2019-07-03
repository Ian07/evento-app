from rest_framework import generics
from api_eventos.utils import AutenticacionSoloGet
from participantes.models import Persona
from participantes.serializers import PersonaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import status
from rest_framework.response import Response
from django.db import IntegrityError

class ListCreatePersonasView(generics.ListCreateAPIView):
    """
    GET personas/
    POST personas/
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = (AutenticacionSoloGet,)

    def post(self, request, *args, **kwargs):
        try:
            nueva_persona = Persona.objects.create(
                documento=request.data["documento"],
                nombre=request.data["nombre"],
                apellido=request.data["apellido"]
            )
            return Response(
                data=PersonaSerializer(nueva_persona).data,
                status=status.HTTP_201_CREATED
            )
        except IntegrityError:
            return Response(
                data={
                    "error": f"Ya existe la persona con el documento: '{request.data['documento']}'.",
                },
                status=status.HTTP_409_CONFLICT
            )


class PersonaDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET personas/:documento/
    PUT personas/:documento/
    DELETE personas/:documento/
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            persona = self.queryset.get(documento=kwargs["documento"])
            return Response(PersonaSerializer(persona).data)
        except Persona.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la persona con el documento: '{kwargs['documento']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, *args, **kwargs):
        try:
            persona = self.queryset.get(documento=kwargs["documento"])
            serializer = PersonaSerializer()
            persona_nueva = serializer.update(persona, request.data)
            return Response(PersonaSerializer(persona_nueva).data)
        except Persona.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la persona con el documento: '{kwargs['documento']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            persona = self.queryset.get(documento=kwargs["documento"])
            persona.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Persona.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la persona con el documento: '{kwargs['documento']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )