# Generated by Django 3.1.12 on 2021-11-22 02:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosticos', '0004_auto_20211107_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosticoobesidad',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de diagnóstico'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='diagnosticoobesidad',
            name='caec',
            field=models.IntegerField(choices=[(0, 'Siempre'), (1, 'Frecuentemente'), (2, 'Algunas veces'), (3, 'No')], verbose_name='Come algún alimento entre comidas'),
        ),
        migrations.AlterField(
            model_name='diagnosticoobesidad',
            name='calc',
            field=models.IntegerField(choices=[(0, 'Siempre'), (1, 'Frecuentemente'), (2, 'Algunas veces'), (3, 'No')], verbose_name='Tiempo que usa dispositivos electrónicos al día'),
        ),
        migrations.AlterField(
            model_name='diagnosticoobesidad',
            name='ch2o',
            field=models.IntegerField(choices=[(0, 'Menos de un litro'), (1, 'Entre 1 y 2 litros'), (2, 'Más de 2 litros')], verbose_name='Consumo de agua diario'),
        ),
        migrations.AlterField(
            model_name='diagnosticoobesidad',
            name='favc',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Si')], verbose_name='Come frecuentemente alimentos con altos niveles calóricos'),
        ),
        migrations.AlterField(
            model_name='diagnosticoobesidad',
            name='fcvc',
            field=models.IntegerField(choices=[(0, 'Nunca'), (1, 'Algunas veces'), (2, 'Siempre')], verbose_name='Come vegetales en sus comidas'),
        ),
        migrations.AlterField(
            model_name='diagnosticoobesidad',
            name='genero',
            field=models.CharField(choices=[(0, 'Mujer'), (1, 'Hombre')], max_length=1, verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='diagnosticoobesidad',
            name='historial_obesidad',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Si')], verbose_name='Historial de sobrepeso en su familia'),
        ),
        migrations.AlterField(
            model_name='diagnosticoobesidad',
            name='mtrans',
            field=models.IntegerField(choices=[(0, 'Automóvil'), (1, 'Motocicleta'), (2, 'Bicicleta'), (3, 'Transporte público'), (4, 'Caminar')], verbose_name='Medio de transporte principal'),
        ),
        migrations.AlterField(
            model_name='diagnosticoobesidad',
            name='nobeyesdad',
            field=models.IntegerField(choices=[(0, 'Peso insuficiente'), (1, 'Peso normal'), (2, 'Sobrepeso nivel 1'), (3, 'Sobrepeso nivel 2'), (4, 'Obesidad tipo 1'), (5, 'Obesidad tipo 2'), (6, 'Obesidad tipo 3')], verbose_name='Peso corporal'),
        ),
        migrations.AlterField(
            model_name='diagnosticoobesidad',
            name='npc',
            field=models.IntegerField(choices=[(0, 'Entre 1 y 2'), (1, 'Tres'), (2, 'Más de tres')], verbose_name='Número de comidas principales al día'),
        ),
    ]