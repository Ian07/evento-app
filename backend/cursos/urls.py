from django.urls import path
from cursos.views import ListCreateCursosView, CursoDetailView, ListCreateClasesView, ClaseDetailView


urlpatterns = [
    path('cursos/', ListCreateCursosView.as_view(), name="cursos-list-create"),
    path('cursos/<int:id>/', CursoDetailView.as_view(), name="cursos-detail"),
    path('clases/', ListCreateClasesView.as_view(), name="clases-list-create"),
    path('clases/<int:id>/', ClaseDetailView.as_view(), name="clases-detail"),
]