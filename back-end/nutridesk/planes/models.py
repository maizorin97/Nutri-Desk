from django.db import models
from django.contrib.auth.models import User

from smae.models import Alimento

class Plan(models.Model):
    idPlan = models.AutoField(primary_key=True, verbose_name="Id Plan")
    idUsuario = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Id Usuario")
    descripcion = models.CharField(verbose_name="Descripción", max_length=500)
    calorias = models.IntegerField(verbose_name="Calorías")

    class Meta:
        ordering = ('-idUsuario',)
        verbose_name_plural = "Planes"

    def __str__(self):
        return 'plan {0} de {1}'.format(self.idPlan,self.idUsuario.username)

class TipoComida(models.Model):
    idTipoComida= models.AutoField(primary_key=True, verbose_name="Id Tipo Comida")
    nombre = models.CharField(verbose_name="Nombre", max_length=20)

    class Meta:
        ordering = ('-idTipoComida',)
        verbose_name_plural = "Tipos de Comidas"

    def __str__(self):
        return '{0}'.format(self.nombre)

class Colacion(models.Model):
    idColacion = models.AutoField(primary_key=True, verbose_name="Id Colacion")
    idPlan = models.ForeignKey(Plan,on_delete=models.CASCADE,verbose_name="Id Plan")
    idAlimento = models.ForeignKey(Alimento,on_delete=models.CASCADE,verbose_name="Id Alimento")
    idTipoComida = models.ForeignKey(TipoComida,on_delete=models.CASCADE,verbose_name="Id Tipo Comida")

    class Meta:
        ordering = ('-idPlan',)
        verbose_name_plural = "Colaciones"

    def __str__(self):
        return 'plan {0} -> {1}, {2}'.format(self.idPlan, self.idAlimento, self.idTipoComida)
