from django.urls import path
from cursos.views import ListCreateCursosView


urlpatterns = [
    path('cursos/', ListCreateCursosView.as_view(), name="cursos-list-create"),
]