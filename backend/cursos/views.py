from rest_framework import generics
from cursos.models import Curso, Clase, Charla
from participantes.models import *
from cursos.serializers import CursoSerializer, ClaseSerializer, CharlaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import status
from rest_framework.response import Response







