from rest_framework import generics
from cursos.models import Charla
from participantes.models import *
from participantes.serializers import DisertanteSerializer
from cursos.serializers import CharlaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import status, APIView
from rest_framework.response import Response


class ListCreateCharlasView(generics.ListCreateAPIView):
    """
    GET charlas/
    POST charlas/
    """
    queryset = Charla.objects.all()
    serializer_class = CharlaSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        
        try:
            disertante = Disertante.objects.get(persona=request.data["documento_disertante"])
        except Disertante.DoesNotExist:    
            return Response(
                data={
                    "error": f"No existe el disertante con documento: '{request.data['documento_disertante']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        nueva_charla = Charla.objects.create(
            dia=request.data["dia"],
            hora_inicio=request.data["hora_inicio"],
            hora_fin=request.data["hora_fin"],
            aula=request.data["aula"],
            nombre=request.data["nombre"],
            descripcion=request.data["descripcion"],
        )
        
        nueva_charla.disertantes.add(disertante)  
        nueva_charla.save()

        return Response(
            data=CharlaSerializer(nueva_charla).data,
            status=status.HTTP_201_CREATED
        )



class CharlaDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET charla/:id/
    PUT charla/:id/
    DELETE charla/:id/
    """
    queryset = Charla.objects.all()
    serializer_class = CharlaSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            charla = self.queryset.get(id=kwargs["id"])
            return Response(CharlaSerializer(charla).data)
        except Charla.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la charla con id: '{kwargs['id']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            ) 

    def put(self, request, *args, **kwargs):
        try:
            charla = self.queryset.get(id=kwargs["id"])
            serializer = CharlaSerializer()
            charla_modificada = serializer.update(charla, request.data)

            if request.POST.get('add_doc_disertante'):
                add_disertante = Disertante.objects.get(persona=request.data["add_doc_disertante"])
                charla_modificada.disertantes.add(add_disertante)  

            if request.POST.get('remove_doc_disertante'):
                remove_disertante = Disertante.objects.get(persona=request.data["remove_doc_disertante"])
                charla_modificada.disertantes.remove(remove_disertante)

            charla_modificada.save()
            return Response(CharlaSerializer(charla_modificada).data)

        except Charla.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la charla con id: '{kwargs['id']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Disertante.DoesNotExist:    
            return Response(
                data={
                    "error": "Uno de los documentos de Disertante no es valido!"
                },
                status=status.HTTP_404_NOT_FOUND
            )    

    def delete(self, request, *args, **kwargs):
        try:
            charla = self.queryset.get(id=kwargs["id"])
            charla.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Charla.DoesNotExist:
            return Response(
                data={
                    "error": f"No existe la charla con id: '{kwargs['id']}'.",
                },
                status=status.HTTP_404_NOT_FOUND
            ) 


class DisertantesList(APIView):
    """
    GET charlas/:id/disertantes
    """
    def get(self, request, *args, **kwargs):
        id_charla = kwargs['id']
        id_disertantes = Charla.objects.filter(id=id_charla).values_list('disertantes', flat=True)
        disertantes = Disertante.objects.filter(id__in=id_disertantes)
        return Response(DisertanteSerializer(disertantes, many=True).data)