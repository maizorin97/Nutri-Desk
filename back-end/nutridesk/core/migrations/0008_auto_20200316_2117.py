# Generated by Django 3.0 on 2020-03-16 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_auto_20200316_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infousuario',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]