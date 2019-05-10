from rest_framework import generics
from cursos.models import Curso
from participantes.models import Persona, Alumno, Profesor, Disertante, Organizador
from cursos.serializers import CursoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import status
from rest_framework.response import Response


class ListCreateCursosView(generics.ListCreateAPIView):
    """
    GET cursos/
    POST cursos/
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        profesor = Profesor.objects.get(
            persona=request.data["documento_profesor"],
        )
        alumno = Alumno.objects.get(
            persona=request.data["documento_alumno"],
        )
        nuevo_curso = Curso.objects.create(
            nombre=request.data["nombre"],
            descripcion=request.data["descripcion"]
        )
        nuevo_curso.profesores.add(profesor)
        nuevo_curso.alumnos.add(alumno)
            
        return Response(
            data=CursoSerializer(nuevo_curso).data,
            status=status.HTTP_201_CREATED
        )