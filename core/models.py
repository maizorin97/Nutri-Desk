from django.db import models
from django.contrib.auth.models import User
from planes.models import Plan

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


class CalendarioUsuario(models.Model):
    idCalendario = models.AutoField(primary_key=True, verbose_name="Id Calendario")
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Id Usuario", unique=True)
    planLunes = models.ForeignKey(Plan, on_delete=models.SET_NULL, verbose_name="Plan de alimentacion lunes", blank=True, null=True, related_name="%(class)s_requests_lunes")
    planMartes = models.ForeignKey(Plan, on_delete=models.SET_NULL, verbose_name="Plan de alimentacion martes", blank=True, null=True, related_name="%(class)s_requests_martes")
    planMiercoles = models.ForeignKey(Plan, on_delete=models.SET_NULL, verbose_name="Plan de alimentacion miércoles", blank=True, null=True, related_name="%(class)s_requests_miercoles")
    planJueves = models.ForeignKey(Plan, on_delete=models.SET_NULL, verbose_name="Plan de alimentacion jueves", blank=True, null=True, related_name="%(class)s_requests_jueves")
    planViernes = models.ForeignKey(Plan, on_delete=models.SET_NULL, verbose_name="Plan de alimentacion viernes", blank=True, null=True, related_name="%(class)s_requests_viernes")
    planSabado = models.ForeignKey(Plan, on_delete=models.SET_NULL, verbose_name="Plan de alimentacion sábado", blank=True, null=True, related_name="%(class)s_requests_sabado")
    planDomingo = models.ForeignKey(Plan, on_delete=models.SET_NULL, verbose_name="Plan de alimentacion domingo", blank=True, null=True, related_name="%(class)s_requests_domingo")
    

    class Meta:
        ordering = ('-idCalendario',)

    def __str__(self):
        return '{0} - {1}'.format(self.idCalendario, self.usuario.username)


class BitacoraUsuario(models.Model):
    idBitacora = models.AutoField(primary_key=True, verbose_name="Id bitacora")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Id usuario")
    fecha_registro = models.DateField(auto_now_add=True, verbose_name="Fecha registro")
    comentario = models.CharField(max_length=200, verbose_name="Comentario usuario", blank=True, null=True)
    ESTADO_ANIMO = (
        ('0', 'Muy triste'),
        ('1', 'Triste'),
        ('2', 'Normal'),
        ('3', 'Feliz'),
        ('4', 'Muy feliz'),
    )
    estado_animo = models.CharField(max_length=20, choices=ESTADO_ANIMO, verbose_name="Estado usuario")
    BINARIO = (
        ('0', 'No'),
        ('1', 'Si'),
    )
    agua = models.IntegerField(choices=BINARIO, verbose_name="¿Tomó agua?")
    ejercicio = models.IntegerField(choices=BINARIO, verbose_name="¿Hizo ejercicio?")
    buen_suenio = models.IntegerField(choices=BINARIO, verbose_name="¿Buen sueño?")
    comer_sano = models.IntegerField(choices=BINARIO, verbose_name="¿Comió saludable?")



    class Meta:
        ordering = ('-idBitacora',)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.idBitacora, self.usuario.username, self.comentario)

