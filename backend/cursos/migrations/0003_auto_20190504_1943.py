# Generated by Django 2.2 on 2019-05-04 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_auto_20190504_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charla',
            name='disertantes',
            field=models.ManyToManyField(db_table='charla_disertante', related_name='charlas', to='participantes.Disertante'),
        ),
    ]
