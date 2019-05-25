"""Aqui se definen los modelos correspondientes a los participantes """
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

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

    class Meta:
        db_table = 'personas'

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
    persona = models.ForeignKey( #TODO seria un One to One ????
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

    class Meta:
        db_table = 'roles'

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

class CustomUserManager(BaseUserManager):

    def crear_usuario(self, username, password, persona):

        user = self.model(
            username = username,
            persona = persona,
            first_name = persona.nombre,
            last_name = persona.apellido,
            email = persona.email
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password):

        user = self.model(
            username = username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, persona):

        user = self.create_user(
            username = username,
            password = password,
            persona = persona,
            first_name = persona.nombre,
            last_name = persona.apellido,
            email = persona.email
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):

        user = self.create_user(
            username = username,
            password = password
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user

class Usuario(Rol, AbstractUser):
    """ Modelo de rol de Usuario. """
    TIPO = 5
    ROLNAME = "Usuario"

    objects = CustomUserManager()

    class Meta:
        db_table = 'usuarios'

for Klass in Rol.__subclasses__():
    Rol.register(Klass)
