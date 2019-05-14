from rest_framework import generics
from cursos.models import Curso, Clase
from participantes.models import Persona, Alumno, Profesor, Disertante, Organizador
from cursos.serializers import CursoSerializer, ClaseSerializer
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
        nuevo_curso = Curso.objects.create(
            nombre=request.data["nombre"],
            descripcion=request.data["descripcion"]
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

            if request.POST.get('documento_profesor'):
                profesor = Profesor.objects.get(persona=request.data["documento_profesor"])
                curso_modificado.profesores.add(profesor)

            if request.POST.get('documento_alumno'):
                alumno = Alumno.objects.get(persona=request.data["documento_alumno"])
                curso_modificado.alumnos.add(alumno)  

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
                    "error": f"No existe el profesor con documento '{request.data['documento_profesor']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Alumno.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe el alumno con documento: '{request.data['documento_alumno']}'.",
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

class ListCreateClasesView(generics.ListCreateAPIView):
    """
    GET clases/
    POST clases/
    """
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        
        try:
            obj_curso = Curso.objects.get(id=request.data["id_curso"])
        except Curso.DoesNotExist:    
            return Response(
                data={
                    "error": f"No existe el curso con id '{request.data['id_curso']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        nueva_clase = Clase.objects.create(
            dia=request.data["dia"],
            hora_inicio=request.data["hora_inicio"],
            hora_fin=request.data["hora_fin"],
            aula=request.data["aula"],
            curso = obj_curso
        )

        return Response(
            data=ClaseSerializer(nueva_clase).data,
            status=status.HTTP_201_CREATED
        )

class ClaseDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET clase/:id/
    PUT clase/:id/
    DELETE clase/:id/
    """
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            clase = self.queryset.get(id=kwargs["id"])
            return Response(ClaseSerializer(clase).data)
        except Clase.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la clase con id: '{kwargs['id']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            ) 

    def put(self, request, *args, **kwargs):
        try:
            clase = self.queryset.get(id=kwargs["id"])
            serializer = ClaseSerializer()
            clase_modificada = serializer.update(clase, request.data)
            
            if request.POST.get('documento_alumno'):
                obj_curso = Curso.objects.get(id=request.data["id_curso"])
                clase_modificada.curso = obj_curso

            if request.POST.get('documento_alumno'):
                alumno = Alumno.objects.get(persona=request.data["documento_alumno"])
                clase_modificada.presentes.add(alumno)  

            clase_modificada.save()
            return Response(ClaseSerializer(clase_modificada).data)

        except Clase.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la clase con id: '{kwargs['id']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Curso.DoesNotExist:    
            return Response(
                data={
                    "error": f"No existe el curso con id '{request.data['id_curso']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )    
        except Alumno.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe el alumno con documento: '{request.data['documento_alumno']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )    

    def delete(self, request, *args, **kwargs):
        try:
            clase = self.queryset.get(id=kwargs["id"])
            clase.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Clase.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la clase con id: '{kwargs['id']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            ) 