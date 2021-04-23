from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Diagnostico(models.Model):
    idDiagnostico = models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento", default=datetime.now)
    altura = models.FloatField(verbose_name="Altura en CM")
    peso = models.FloatField(verbose_name="Peso en KG")
    SEXOS = (
        ('H','Hombre'),
        ('M','Mujer'),
    )
    sexo = models.CharField(max_length=1, choices=SEXOS, verbose_name="Sexo")
    pres_hi = models.IntegerField(verbose_name="P.A. Sistólica mmHg")
    pres_lo = models.IntegerField(verbose_name="P.A. Diastólica mmHg")
    TRES = (
        (0,'Normal'),
        (1,'Arriba de lo normal'),
        (2,'Muy arriba de lo normal'),
    )
    glucosa = models.IntegerField(choices=TRES, verbose_name="Nivel de glucosa")
    colesterol = models.IntegerField(choices=TRES, verbose_name="Nivel de colesterol")
    BINARIO = (
        (0,'No'),
        (1,'Si'),
    )
    fumador = models.IntegerField(choices=BINARIO, verbose_name="Fumador")
    alcoholico = models.IntegerField(choices=BINARIO, verbose_name="Acoholico")
    deporte = models.IntegerField(choices=BINARIO, verbose_name="Hace deporte")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de diagnóstico")
    BINARIO2 = (
        (0,'Negativo'),
        (1,'Positivo'),
    )
    resultado = models.IntegerField(choices=BINARIO2,verbose_name="Resultado del diagnostico")

    class Meta:
        ordering = ('-idUsuario',)

    def __str__(self):
        return '{0}'.format(self.idUsuario.username)