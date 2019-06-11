from django.urls import path
from participantes.views.personas import *
from participantes.views.roles import *


urlpatterns = [
    path('personas/', ListCreatePersonasView.as_view(), name="personas-list-create"),
    path('personas/<int:documento>/', PersonaDetailView.as_view(), name="personas-detail"),
    path('alumnos/', ListCreateAlumnoView.as_view(), name="alumnos-list-create"),
    path('alumnos/<int:documento>/', AlumnoDetailView.as_view(), name="alumnos-detail"),
    path('profesores/', ListCreateProfesorView.as_view(), name="profesores-list-create"),
    path('profesores/<int:documento>/', ProfesorDetailView.as_view(), name="profesores-detail"),
    path('disertantes/', ListCreateDisertanteView.as_view(), name="disertantes-list-create"),
    path('disertantes/<int:documento>/', DisertanteDetailView.as_view(), name="disertantes-detail"),
    path('organizadores/', ListCreateOrganizadorView.as_view(), name="organizadores-list-create"),
    path('organizadores/<int:documento>/', OrganizadorDetailView.as_view(), name="organizadores-detail"),
    path('usuarios/', ListCreateUsuarioView.as_view(), name="usuarios-list-create"),
    path('usuarios/<int:documento>/', UsuariorDetailView.as_view(), name="usuarios-detail"),
    path('registrar_usuario/', UserList.as_view())
]