from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from participantes.models import (
    Persona, Alumno, Profesor, Disertante, Organizador, Usuario
)

#Agrego a la admin de Django la posiblidad de ABM objetos del tipo Persona
admin.site.register(Persona)

#Agrego a la admin de Django la posiblidad de ABM objetos del tipo Alumno
admin.site.register(Alumno)

#Agrego a la admin de Django la posiblidad de ABM objetos del tipo Profesor
admin.site.register(Profesor)

#Agrego a la admin de Django la posiblidad de ABM objetos del tipo Disertante
admin.site.register(Disertante)

#Agrego a la admin de Django la posiblidad de ABM objetos del tipo Organizador
admin.site.register(Organizador)

#Agrego a la admin de Django la posiblidad de ABM objetos del tipo Usuario
admin.site.register(Usuario, UserAdmin)