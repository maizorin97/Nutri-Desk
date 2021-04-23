# Generated by Django 3.0 on 2020-03-17 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('smae', '0002_auto_20200308_0504'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoColacion',
            fields=[
                ('idTipoColacion', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Tipo Colacion')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
            ],
            options={
                'ordering': ('-idTipoColacion',),
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('idPlan', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Plan')),
                ('descripcion', models.CharField(max_length=500, verbose_name='Descripción')),
                ('calorias', models.IntegerField(verbose_name='Calorías')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Id Usuario')),
            ],
            options={
                'ordering': ('-idUsuario',),
            },
        ),
        migrations.CreateModel(
            name='Colacion',
            fields=[
                ('idColacion', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Colacion')),
                ('idAlimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smae.Alimento', verbose_name='Id Alimento')),
                ('idPlan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planes.Plan', verbose_name='Id Plan')),
                ('idTipoColacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planes.TipoColacion', verbose_name='Id Tipo Colacion')),
            ],
            options={
                'ordering': ('-idPlan',),
            },
        ),
    ]