from django.urls import path
from participantes.views import ListPersonasView


urlpatterns = [
    path('personas/', ListPersonasView.as_view(), name="personas-all"),
]