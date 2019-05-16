from django.urls import path
from cursos.views.cursos import *
from cursos.views.clases import *
from cursos.views.charlas import *


urlpatterns = [
    path('cursos/', ListCreateCursosView.as_view(), name="cursos-list-create"),
    path('cursos/<int:id>/', CursoDetailView.as_view(), name="cursos-detail"),
    path('cursos/<int:id>/profesores/', ProfesoresList.as_view(), name="curso-profesores-list"),
    path('cursos/<int:id>/alumnos/', AlumnosList.as_view(), name="curso-alumnos-list"),
    path('cursos/<int:id>/clases/', ClasesList.as_view(), name="curso-clases-list"),
    path('clases/', ListCreateClasesView.as_view(), name="clases-list-create"),
    path('clases/<int:id>/', ClaseDetailView.as_view(), name="clases-detail"),
    path('charlas/', ListCreateCharlasView.as_view(), name="charlas-list-create"),
    path('charlas/<int:id>/', CharlaDetailView.as_view(), name="charlas-detail"),
]