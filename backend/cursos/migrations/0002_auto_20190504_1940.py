# Generated by Django 2.2 on 2019-05-04 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participantes', '0001_initial'),
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clase',
            name='presentes',
            field=models.ManyToManyField(db_table='asistencias', related_name='asistencias', to='participantes.Alumno'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='alumnos',
            field=models.ManyToManyField(db_table='curso_alumnos', related_name='cursos', to='participantes.Alumno'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='profesores',
            field=models.ManyToManyField(db_table='curso_profesor', related_name='cursos', to='participantes.Profesor'),
        ),
    ]