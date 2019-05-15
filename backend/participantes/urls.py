from django.urls import path
from participantes.views.personas import *
from participantes.views.roles import *


urlpatterns = [
    path('personas/', ListCreatePersonasView.as_view(), name="personas-list-create"),
    path('personas/<int:documento>/', PersonaDetailView.as_view(), name="personas-detail"),
    path('alumno/', ListCreateAlumnoView.as_view(), name="alumno-list-create"),
    path('profesor/', ListCreateProfesorView.as_view(), name="profesor-list-create"),
    path('disertante/', ListCreateDisertanteView.as_view(), name="disertante-list-create"),
    path('organizador/', ListCreateOrganizadorView.as_view(), name="organizador-list-create")
]