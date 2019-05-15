from rest_framework import generics
from participantes.models import Alumno, Profesor, Disertante, Organizador
from participantes.serializers import AlumnoSerializer, ProfesorSerializer, DisertanteSerializer, OrganizadorSerializer
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