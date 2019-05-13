from rest_framework import generics
from participantes.models import Persona, Alumno, Profesor, Disertante, Organizador
from participantes.serializers import PersonaSerializer, AlumnoSerializer, ProfesorSerializer, DisertanteSerializer, OrganizadorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import status
from rest_framework.response import Response


class ListCreateAlumnoView(generics.ListCreateAPIView):
    """
    GET alumnos/
    POST alumno/
    """
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            persona = Persona.objects.get(documento=request.data["documento"])
        except Persona.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la persona con el documento: '{kwargs['documento']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        nuevo_alumno = Alumno.objects.create(
            persona = persona
        )
        return Response(
            data=AlumnoSerializer(nuevo_alumno).data,
            status=status.HTTP_201_CREATED
        )


class ListCreateProfesorView(generics.ListCreateAPIView):
    """
    GET profesores/
    POST profesor/
    """
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            persona = Persona.objects.get(documento=request.data["documento"])
        except Persona.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la persona con el documento: '{kwargs['documento']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        nuevo_profesor = Profesor.objects.create(
            persona = persona
        )
        return Response(
            data=ProfesorSerializer(nuevo_profesor).data,
            status=status.HTTP_201_CREATED
        )


class ListCreateDisertanteView(generics.ListCreateAPIView):
    """
    GET disertantes/
    POST disertante/
    """
    queryset = Disertante.objects.all()
    serializer_class = DisertanteSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            persona = Persona.objects.get(documento=request.data["documento"])
        except Persona.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la persona con el documento: '{kwargs['documento']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        nuevo_disertante = Disertante.objects.create(
            persona = persona
        )
        return Response(
            data=DisertanteSerializer(nuevo_disertante).data,
            status=status.HTTP_201_CREATED
        )


class ListCreateOrganizadorView(generics.ListCreateAPIView):
    """
    GET organizadores/
    POST organizador/
    """
    queryset = Organizador.objects.all()
    serializer_class = OrganizadorSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            persona = Persona.objects.get(documento=request.data["documento"])
        except Persona.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la persona con el documento: '{kwargs['documento']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        nuevo_organizador = Organizador.objects.create(
            persona = persona
        )
        return Response(
            data=OrganizadorSerializer(nuevo_organizador).data,
            status=status.HTTP_201_CREATED
        )


class ListCreatePersonasView(generics.ListCreateAPIView):
    """
    GET personas/
    POST personas/
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        nueva_persona = Persona.objects.create(
            documento=request.data["documento"],
            nombre=request.data["nombre"],
            apellido=request.data["apellido"]
        )
        return Response(
            data=PersonaSerializer(nueva_persona).data,
            status=status.HTTP_201_CREATED
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


