from django.urls import path
from participantes.views import ListCreatePersonasView, PersonaDetailView, ListCreateProfesorView


urlpatterns = [
    path('personas/', ListCreatePersonasView.as_view(), name="personas-list-create"),
    path('personas/<int:documento>/', PersonaDetailView.as_view(), name="personas-detail"),
    path('profesor/', ListCreateProfesorView.as_view(), name="profesor-list-create")
]