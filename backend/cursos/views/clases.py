from rest_framework import generics
from cursos.models import Clase, Curso
from participantes.models import *
from cursos.serializers import  ClaseSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import status
from rest_framework.response import Response


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
            
            if request.POST.get('id_curso'):
                obj_curso = Curso.objects.get(id=request.data["id_curso"])
                clase_modificada.curso = obj_curso

            if request.POST.get('add_doc_alumno'):
                alumno = Alumno.objects.get(persona=request.data["add_doc_alumno"])
                clase_modificada.presentes.add(alumno) 

            if request.POST.get('remove_doc_alumno'):
                alumno = Alumno.objects.get(persona=request.data["remove_doc_alumno"])
                clase_modificada.presentes.remove(alumno) 

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
                    "error": "Uno de los documentos de Alumno no es valido!"
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