from rest_framework import generics
from cursos.models import Curso
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
        nueva_curso = Curso.objects.create(
            nombre=request.data["nombre"],
            descripcion=request.data["descripcion"],
            #profesores=request.data["profesores"]
        )
        return Response(
            data=CursoSerializer(nueva_curso).data,
            status=status.HTTP_201_CREATED
        )