from rest_framework import generics
from cursos.models import Curso, Clase
from participantes.models import *
from cursos.serializers import CursoSerializer, ClaseSerializer
from participantes.serializers import ProfesorSerializer, AlumnoSerializer
from api_eventos.utils import AutenticacionSoloPost
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import status, APIView
from rest_framework.response import Response

class ListCreateCursosView(generics.ListCreateAPIView):
    """
    GET cursos/
    POST cursos/
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = (AutenticacionSoloPost,)

    def post(self, request, *args, **kwargs):
        nuevo_curso = Curso.objects.create(
            nombre=request.data["nombre"],
            slogan=request.data["slogan"],
            descripcion=request.data["descripcion"],
            imagen=request.data["imagen"]
        )
        try:
            if request.POST.get('documento_profesor'):
                profesor = Profesor.objects.get(persona=request.data["documento_profesor"])
                nuevo_curso.profesores.add(profesor)
            if request.POST.get('documento_alumno'):
                alumno = Alumno.objects.get(persona=request.data["documento_alumno"])
                nuevo_curso.alumnos.add(alumno)
        except Profesor.DoesNotExist:    
            return Response(
                data={
                    "error": f"No existe el profesor con documento '{request.data['documento_profesor']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Alumno.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe el alumno con documento '{request.data['documento_alumno']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
            
        return Response(
            data=CursoSerializer(nuevo_curso).data,
            status=status.HTTP_201_CREATED
        )

class CursoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET cursos/:id/
    PUT cursos/:id/
    DELETE cursos/:id/
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            curso = self.queryset.get(id=kwargs["id"])
            return Response(CursoSerializer(curso).data)
        except Curso.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe el curso con id: '{kwargs['id']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            ) 

    def put(self, request, *args, **kwargs):
        try:
            curso = self.queryset.get(id=kwargs["id"])
            serializer = CursoSerializer()
            curso_modificado = serializer.update(curso, request.data)

            if request.POST.get('add_doc_profesor'):
                profesor = Profesor.objects.get(persona=request.data["add_doc_profesor"])
                curso_modificado.profesores.add(profesor)

            if request.POST.get('remove_doc_profesor'):
                profesor = Profesor.objects.get(persona=request.data["remove_doc_profesor"])
                curso_modificado.profesores.remove(profesor)

            if request.POST.get('add_doc_alumno'):
                alumno = Alumno.objects.get(persona=request.data["add_doc_alumno"])
                curso_modificado.alumnos.add(alumno)  
            
            if request.POST.get('remove_doc_alumno'):
                alumno = Alumno.objects.get(persona=request.data["remove_doc_alumno"])
                curso_modificado.alumnos.remove(alumno)  

            curso_modificado.save()
            return Response(CursoSerializer(curso_modificado).data)

        except Curso.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe el curso con id: '{kwargs['id']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Profesor.DoesNotExist:    
            return Response(
                data={
                    "error": "Uno de los documentos de Profesor no es valido!"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Alumno.DoesNotExist:
            return Response(
                data={
                    "error": "Uno de los documentos de Alumno no es valido!"
                },
                status=status.HTTP_404_NOT_FOUND
            )    

    def delete(self, request, *args, **kwargs):
        try:
            curso = self.queryset.get(id=kwargs["id"])
            curso.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Curso.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe el curso con id: '{kwargs['id']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )    


class ProfesoresList(APIView):
    """
    GET cursos/:id/profesores
    """
    def get(self, request, *args, **kwargs):
        id_curso = kwargs['id']
        id_profesores = Curso.objects.filter(id=id_curso).values_list('profesores', flat=True)
        profesores = Profesor.objects.filter(id__in=id_profesores)
        return Response(ProfesorSerializer(profesores, many=True).data)


class AlumnosList(APIView):
    """
    GET cursos/:id/alumnos
    """
    def get(self, request, *args, **kwargs):
        id_curso = kwargs['id']
        id_alumnos = Curso.objects.filter(id=id_curso).values_list('alumnos', flat=True)
        alumnos = Alumno.objects.filter(id__in=id_alumnos)
        return Response(AlumnoSerializer(alumnos, many=True).data)
        

class ClasesList(APIView):
    """
    GET cursos/:id/clases
    """
    def get(self, request, *args, **kwargs):
        id_curso = kwargs['id']
        id_clases = Curso.objects.filter(id=id_curso).values_list('clases', flat=True)
        clases = Clase.objects.filter(id__in=id_clases)
        return Response(ClaseSerializer(clases, many=True).data)