from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

class InfoUsuario(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='Usuario',null=False,blank=False,primary_key=True)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento", default=datetime.now)
    altura = models.FloatField(verbose_name="Altura en CM")
    peso = models.FloatField(verbose_name="Peso en KG")
    SEXOS = (
        ('H','Hombre'),
        ('M','Mujer'),
    )
    sexo = models.CharField(max_length=1, choices=SEXOS)

    class Meta:
        ordering = ('-usuario',)

    def __str__(self):
        return '{0}'.format(self.usuario.username)

class PesosUsuario(models.Model):
    idPeso = models.AutoField(primary_key=True, verbose_name="Id Peso")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Id Usuario")
    peso = models.FloatField(verbose_name="Peso en KG")
    fecha_creacion = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-usuario',)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.usuario.username, self.fecha_creacion ,self.peso)

