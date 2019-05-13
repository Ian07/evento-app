from django.urls import path
from cursos.views import ListCreateCursosView, CursoDetailView


urlpatterns = [
    path('cursos/', ListCreateCursosView.as_view(), name="cursos-list-create"),
    path('cursos/<int:id>/', CursoDetailView.as_view(), name="cursos-detail"),
]