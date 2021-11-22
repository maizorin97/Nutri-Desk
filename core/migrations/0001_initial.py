# Generated by Django 3.1.12 on 2021-11-22 22:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('planes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoUsuario',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user', verbose_name='Usuario')),
                ('fecha_nacimiento', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de nacimiento')),
                ('altura', models.FloatField(verbose_name='Altura en CM')),
                ('peso', models.FloatField(verbose_name='Peso en KG')),
                ('sexo', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer')], max_length=1)),
            ],
            options={
                'ordering': ('-usuario',),
            },
        ),
        migrations.CreateModel(
            name='PesosUsuario',
            fields=[
                ('idPeso', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Peso')),
                ('peso', models.FloatField(verbose_name='Peso en KG')),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Id Usuario')),
            ],
            options={
                'ordering': ('-usuario',),
            },
        ),
        migrations.CreateModel(
            name='CalendarioUsuario',
            fields=[
                ('idCalendario', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Calendario')),
                ('planDomingo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='calendariousuario_requests_domingo', to='planes.plan', verbose_name='Plan de alimentacion domingo')),
                ('planJueves', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='calendariousuario_requests_jueves', to='planes.plan', verbose_name='Plan de alimentacion jueves')),
                ('planLunes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='calendariousuario_requests_lunes', to='planes.plan', verbose_name='Plan de alimentacion lunes')),
                ('planMartes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='calendariousuario_requests_martes', to='planes.plan', verbose_name='Plan de alimentacion martes')),
                ('planMiercoles', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='calendariousuario_requests_miercoles', to='planes.plan', verbose_name='Plan de alimentacion miércoles')),
                ('planSabado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='calendariousuario_requests_sabado', to='planes.plan', verbose_name='Plan de alimentacion sábado')),
                ('planViernes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='calendariousuario_requests_viernes', to='planes.plan', verbose_name='Plan de alimentacion viernes')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Id Usuario')),
            ],
            options={
                'ordering': ('-idCalendario',),
            },
        ),
        migrations.CreateModel(
            name='BitacoraUsuario',
            fields=[
                ('idBitacora', models.AutoField(primary_key=True, serialize=False, verbose_name='Id bitacora')),
                ('fecha_registro', models.DateField(auto_now_add=True, verbose_name='Fecha registro')),
                ('comentario', models.CharField(blank=True, max_length=200, null=True, verbose_name='Comentario usuario')),
                ('estado_animo', models.CharField(choices=[('0', 'Muy triste'), ('1', 'Triste'), ('2', 'Normal'), ('2', 'Feliz'), ('2', 'Muy feliz')], max_length=20, verbose_name='Comentario usuario')),
                ('agua', models.IntegerField(choices=[('0', 'No'), ('1', 'Si')], verbose_name='¿Tomó agua?')),
                ('ejercicio', models.IntegerField(choices=[('0', 'No'), ('1', 'Si')], verbose_name='¿Hizo ejercicio?')),
                ('buen_suenio', models.IntegerField(choices=[('0', 'No'), ('1', 'Si')], verbose_name='¿Buen sueño?')),
                ('comer_sano', models.IntegerField(choices=[('0', 'No'), ('1', 'Si')], verbose_name='¿Comió saludable?')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Id usuario')),
            ],
            options={
                'ordering': ('-idBitacora',),
            },
        ),
    ]
