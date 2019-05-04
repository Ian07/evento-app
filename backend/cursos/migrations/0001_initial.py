# Generated by Django 2.2 on 2019-05-04 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('participantes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=800)),
                ('alumnos', models.ManyToManyField(to='participantes.Alumno')),
                ('profesores', models.ManyToManyField(to='participantes.Profesor')),
            ],
            options={
                'db_table': 'cursos',
            },
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('aula', models.CharField(max_length=50)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clases', to='cursos.Curso')),
            ],
            options={
                'db_table': 'clases',
            },
        ),
        migrations.CreateModel(
            name='Charla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('aula', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=800)),
                ('disertantes', models.ManyToManyField(to='participantes.Disertante')),
            ],
            options={
                'db_table': 'charlas',
            },
        ),
    ]
