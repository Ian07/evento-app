from django.contrib import admin
from cursos.models import Curso, Charla, Clase

#Agrego a la admin de Django la posiblidad de ABM objetos del tipo Curso
admin.site.register(Curso)

#Agrego a la admin de Django la posiblidad de ABM objetos del tipo Clase
admin.site.register(Clase)

#Agrego a la admin de Django la posiblidad de ABM objetos del tipo Charla
admin.site.register(Charla)

