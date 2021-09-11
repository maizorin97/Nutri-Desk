# Generated by Django 3.1.12 on 2021-09-07 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0008_auto_20200316_2117'),
    ]

    operations = [
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
    ]
