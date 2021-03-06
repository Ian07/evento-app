from django.db import models
from participantes.models import Profesor, Disertante, Alumno


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    slogan = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.TextField(max_length=800)
    imagen = models.ImageField(upload_to='imagenes')
    profesores = models.ManyToManyField(Profesor, related_name="cursos", db_table="curso_profesor")
    alumnos = models.ManyToManyField(Alumno, related_name="cursos", db_table="curso_alumnos", blank=True)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        db_table = 'cursos'

class Encuentro(models.Model):
    dia = models.DateField()
    hora_inicio = models.TimeField() # hora y fecha separadas? ventaja en busqueda por solo horarios (Dame todo lo que sea de 16 a 18)
    hora_fin = models.TimeField()
    aula = models.CharField(max_length=50) # Vale hacer una clase aula?

    class Meta:
        abstract = True

class Clase(Encuentro):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='clases')
    presentes = models.ManyToManyField(Alumno, related_name="asistencias", db_table="asistencias", blank=True)

    def __str__(self):
        return f"{self.curso} - {self.dia} - {self.hora_inicio} - {self.aula}"

    class Meta:
        db_table = 'clases'

class Charla(Encuentro):
    disertantes = models.ManyToManyField(Disertante, related_name="charlas", db_table="charla_disertante")
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=800)

    class Meta:
        db_table = 'charlas'