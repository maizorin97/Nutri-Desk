# Generated by Django 3.1.12 on 2021-11-30 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosticos', '0005_auto_20211121_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosticoobesidad',
            name='calc',
            field=models.IntegerField(choices=[(0, 'Siempre'), (1, 'Frecuentemente'), (2, 'Algunas veces'), (3, 'No')], verbose_name='Frecuencia de consumo de alcohol'),
        ),
        migrations.AlterField(
            model_name='diagnosticoobesidad',
            name='genero',
            field=models.IntegerField(choices=[(0, 'Mujer'), (1, 'Hombre')], verbose_name='Genero'),
        ),
    ]
