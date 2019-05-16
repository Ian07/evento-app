from rest_framework import generics
from participantes.models import Persona, Alumno, Profesor, Disertante, Organizador, Usuario
from participantes.serializers import AlumnoSerializer, ProfesorSerializer, DisertanteSerializer, OrganizadorSerializer, UsuarioSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import status
from rest_framework.response import Response


class ListCreateAlumnoView(generics.ListCreateAPIView):
    """
    GET alumnos/
    POST alumnos/
    """
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            obj_persona = Persona.objects.get(documento=request.data["documento"])
        except Persona.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la persona con el documento: '{kwargs['documento']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        nuevo_alumno = Alumno.objects.create(
            persona = obj_persona
        )
        return Response(
            data=AlumnoSerializer(nuevo_alumno).data,
            status=status.HTTP_201_CREATED
        )


class AlumnoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET alumnos/:documento/
    DELETE alumnos/:documento/
    """
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            obj_persona = Persona.objects.get(documento=kwargs["documento"])
            alumno = self.queryset.get(persona=obj_persona)
            return Response(AlumnoSerializer(alumno).data)
        except Persona.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la persona con el documento: '{kwargs['documento']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )    
        except Alumno.DoesNotExist:
            return Response(
                data={
                    "error": f"La persona con documento: '{kwargs['documento']}', NO posee el rol Alumno.",
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            obj_persona = Persona.objects.get(documento=kwargs["documento"])
            alumno = self.queryset.get(persona=obj_persona)
            alumno.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Persona.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la persona con el documento: '{kwargs['documento']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Alumno.DoesNotExist:
            return Response(
                data={
                    "error": f"La persona con documento: '{kwargs['documento']}', NO posee el rol Alumno.",
                },
                status=status.HTTP_404_NOT_FOUND
            )


class ListCreateProfesorView(generics.ListCreateAPIView):
    """
    GET profesores/
    POST profesores/
    """
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            obj_persona = Persona.objects.get(documento=request.data["documento"])
        except Persona.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la persona con el documento: '{kwargs['documento']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        nuevo_profesor = Profesor.objects.create(
            persona = obj_persona
        )
        return Response(
            data=ProfesorSerializer(nuevo_profesor).data,
            status=status.HTTP_201_CREATED
        )


class ProfesorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET profesores/:documento/
    DELETE profesores/:documento/
    """
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            obj_persona = Persona.objects.get(documento=kwargs["documento"])
            profesor = self.queryset.get(persona=obj_persona)
            return Response(ProfesorSerializer(profesor).data)
        except Persona.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la persona con el documento: '{kwargs['documento']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )    
        except Profesor.DoesNotExist:
            return Response(
                data={
                    "error": f"La persona con documento: '{kwargs['documento']}', NO posee el rol Profesor.",
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            obj_persona = Persona.objects.get(documento=kwargs["documento"])
            profesor = self.queryset.get(persona=obj_persona)
            profesor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Persona.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la persona con el documento: '{kwargs['documento']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Profesor.DoesNotExist:
            return Response(
                data={
                    "error": f"La persona con documento: '{kwargs['documento']}', NO posee el rol Profesor.",
                },
                status=status.HTTP_404_NOT_FOUND
            )


class ListCreateDisertanteView(generics.ListCreateAPIView):
    """
    GET disertantes/
    POST disertantes/
    """
    queryset = Disertante.objects.all()
    serializer_class = DisertanteSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            obj_persona = Persona.objects.get(documento=request.data["documento"])
        except Persona.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la persona con el documento: '{kwargs['documento']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        nuevo_disertante = Disertante.objects.create(
            persona = obj_persona
        )
        return Response(
            data=DisertanteSerializer(nuevo_disertante).data,
            status=status.HTTP_201_CREATED
        )


class DisertanteDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET disertantes/:documento/
    DELETE disertantes/:documento/
    """
    queryset = Disertante.objects.all()
    serializer_class = DisertanteSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            obj_persona = Persona.objects.get(documento=kwargs["documento"])
            disertante = self.queryset.get(persona=obj_persona)
            return Response(DisertanteSerializer(disertante).data)
        except Persona.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la persona con el documento: '{kwargs['documento']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )    
        except Disertante.DoesNotExist:
            return Response(
                data={
                    "error": f"La persona con documento: '{kwargs['documento']}', NO posee el rol Disertante.",
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            obj_persona = Persona.objects.get(documento=kwargs["documento"])
            disertante = self.queryset.get(persona=obj_persona)
            disertante.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Persona.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la persona con el documento: '{kwargs['documento']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Disertante.DoesNotExist:
            return Response(
                data={
                    "error": f"La persona con documento: '{kwargs['documento']}', NO posee el rol Disertante.",
                },
                status=status.HTTP_404_NOT_FOUND
            )


class ListCreateOrganizadorView(generics.ListCreateAPIView):
    """
    GET organizadores/
    POST organizadores/
    """
    queryset = Organizador.objects.all()
    serializer_class = OrganizadorSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            obj_persona = Persona.objects.get(documento=request.data["documento"])
        except Persona.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la persona con el documento: '{kwargs['documento']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        nuevo_organizador = Organizador.objects.create(
            persona = obj_persona
        )
        return Response(
            data=OrganizadorSerializer(nuevo_organizador).data,
            status=status.HTTP_201_CREATED
        )


class OrganizadorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET organizadores/:documento/
    DELETE organizadores/:documento/
    """
    queryset = Organizador.objects.all()
    serializer_class = OrganizadorSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            obj_persona = Persona.objects.get(documento=kwargs["documento"])
            organizador = self.queryset.get(persona=obj_persona)
            return Response(OrganizadorSerializer(organizador).data)
        except Persona.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la persona con el documento: '{kwargs['documento']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )    
        except Organizador.DoesNotExist:
            return Response(
                data={
                    "error": f"La persona con documento: '{kwargs['documento']}', NO posee el rol Organizador.",
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            obj_persona = Persona.objects.get(documento=kwargs["documento"])
            organizador = self.queryset.get(persona=obj_persona)
            organizador.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Persona.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la persona con el documento: '{kwargs['documento']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Organizador.DoesNotExist:
            return Response(
                data={
                    "error": f"La persona con documento: '{kwargs['documento']}', NO posee el rol Organizador.",
                },
                status=status.HTTP_404_NOT_FOUND
            )


class ListCreateUsuarioView(generics.ListCreateAPIView):
    """
    GET usuarios/
    POST usuarios/
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            obj_persona = Persona.objects.get(documento=request.data["documento"])
        except Persona.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la persona con el documento: '{kwargs['documento']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        nuevo_usuario = Usuario.objects.create(
            persona = obj_persona
        )
        return Response(
            data=UsuarioSerializer(nuevo_usuario).data,
            status=status.HTTP_201_CREATED
        )


class UsuariorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET usuarios/:documento/
    DELETE usuarios/:documento/
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            obj_persona = Persona.objects.get(documento=kwargs["documento"])
            usuario = self.queryset.get(persona=obj_persona)
            return Response(UsuarioSerializer(usuario).data)
        except Persona.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la persona con el documento: '{kwargs['documento']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )    
        except Usuario.DoesNotExist:
            return Response(
                data={
                    "error": f"La persona con documento: '{kwargs['documento']}', NO posee el rol Usuario.",
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            obj_persona = Persona.objects.get(documento=kwargs["documento"])
            usuario = self.queryset.get(persona=obj_persona)
            usuario.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Persona.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la persona con el documento: '{kwargs['documento']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Usuario.DoesNotExist:
            return Response(
                data={
                    "error": f"La persona con documento: '{kwargs['documento']}', NO posee el rol Usuario.",
                },
                status=status.HTTP_404_NOT_FOUND
            )