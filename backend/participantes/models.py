"""Aqui se definen los modelos correspondientes a los participantes """
from django.db import models
from django.contrib.auth.models import AbstractUser

class Persona(models.Model):
    """
    Modelo representativo de una persona participante del evento.
    """
    documento = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.documento} - {self.get_nombre_completo()}"

    def get_nombre_completo(self):
        """
        Metodo que permite obtener el nombre completo.
        """
        return f"{self.nombre} {self.apellido}"

    def save(self):
        # pylint: disable=W0221
        """
        Metodo que permite modificar el proceso de guardado.
        """
        if Persona.objects.filter(documento=self.documento).exists():
            raise Exception("La persona ya se encuentra registrada")
        super().save()

    def como(self, klass):
        """ 
        Retorna una instancia de un rol asociado a una persona con la ayuda 
        del método related de la clase Rol.
        Args
            Klass (string): nombre de una subclase de Rol
        Returns
            instancia de alguna subclase de Rol
        """
        return self.roles.get(tipo=klass.TIPO).related()

    def agregar_rol(self, rol):
        """ Agrega un rol a una persona.
        **Args:**
            - rol (string): rol
        """
        if not self.sos(rol.__class__):
            rol.persona = self
            rol.save()

    def eliminar_rol(self, rol):
        
        if self.sos(rol.__class__):
            rol.delete()
        
        if len(self.roles_related()) == 0:
            self.delete()

    def roles_related(self):
        """ Retorna la colección de roles asociados a una persona. """
        return [rol.related() for rol in self.roles.all()]

    def sos(self, klass):
        """ Recibe una subclase de rol y retorna True si la persona está asociada y False si no.
        **Args:**
            - Klass (string): subclase de Rol
        **Returns:**
            - bool
        """
        return any([isinstance(rol, klass) for rol in self.roles_related()])

class Rol(models.Model):
    """
    Modelo genérico para la gestión de roles de participantes.
    """
    TIPO = 0
    ROLNAME = "Rol"

    TIPOS = [
        (0, ROLNAME)
    ]

    tipo = models.PositiveSmallIntegerField(choices=TIPOS)
    persona = models.ForeignKey(
        Persona,
        related_name="roles",
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return "{}".format(self.ROLNAME)
    
    @property
    def nombre(self):
        """ Retorna el nombre de la persona """
        return self.persona.nombre

    @property
    def apellido(self):
        """ Retorna el apellido de la persona """
        return self.persona.apellido
    
    @property
    def documento(self):
        """ Retorna el documento de la persona """
        return self.persona.documento

    def save(self, *args, **kwargs):
        # pylint: disable=W0221
        if self.pk is None:
            self.tipo = self.__class__.TIPO
        super(Rol, self).save(*args, **kwargs)

    def related(self):
        """ Retorna una instancia de una subclase de Rol """
        return self.__class__ != Rol and self or getattr(self, self.get_tipo_display())

    @classmethod
    def register(cls, klass):
        """ Método de clase para registrar TIPOS """
        cls.TIPOS.append((klass.TIPO, klass.__name__.lower()))

class Alumno(Rol):
    """ Modelo de rol de Alumno. """
    TIPO = 1
    ROLNAME = "Alumno"

    class Meta:
        db_table = 'alumnos'

class Profesor(Rol):
    """ Modelo de rol de Profesor. """
    TIPO = 2
    ROLNAME = "Profesor"

    class Meta:
        db_table = 'profesores'

class Disertante(Rol):
    """ Modelo de rol de Disertante. """
    TIPO = 3
    ROLNAME = "Disertante"

    class Meta:
        db_table = 'disertantes'

class Organizador(Rol):
    """ Modelo de rol de Organizador. """
    TIPO = 4
    ROLNAME = "Organizador"

    class Meta:
        db_table = 'organizadores'

class Usuario(Rol, AbstractUser):
    """ Modelo de rol de Usuario. """
    TIPO = 5
    ROLNAME = "Usuario"

    class Meta:
        db_table = 'usuarios'

for Klass in Rol.__subclasses__():
    Rol.register(Klass)
