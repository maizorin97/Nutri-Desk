# Generated by Django 3.1.13 on 2021-11-23 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211122_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='infousuario',
            name='foto',
            field=models.ImageField(blank=True, default='default.png', upload_to='perfiles'),
        ),
        migrations.AlterField(
            model_name='bitacorausuario',
            name='estado_animo',
            field=models.CharField(choices=[('0', 'Muy triste'), ('1', 'Triste'), ('2', 'Normal'), ('3', 'Feliz'), ('4', 'Muy feliz')], max_length=20, verbose_name='Estado usuario'),
        ),
    ]