# Generated by Django 3.0 on 2020-03-07 01:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20200307_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('altura', models.FloatField(verbose_name='Altura en CM')),
                ('peso', models.FloatField(verbose_name='Peso en KG')),
                ('sexo', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer')], max_length=1)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]