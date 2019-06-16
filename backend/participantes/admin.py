from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
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


# https://stackoverflow.com/questions/15012235/using-django-auth-useradmin-for-a-custom-user-model
class UsuarioChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Usuario

class MyUserAdmin(UserAdmin):
    form = UsuarioChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('tipo','persona',)}),
    )


#Agrego a la admin de Django la posiblidad de ABM objetos del tipo Usuario
admin.site.register(Usuario, MyUserAdmin)