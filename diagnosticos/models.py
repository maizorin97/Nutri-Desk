from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class DiagnosticoCardio(models.Model):
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


class DiagnosticoObesidad(models.Model):
    idDiagnostico = models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    GENEROS = (
        (1,'Mujer'),
        (0,'Hombre'),
    )
    genero = models.CharField(max_length=1, choices=GENEROS, verbose_name="Genero")
    edad = models.DateField(verbose_name="Fecha de nacimiento", default=datetime.now)
    altura = models.FloatField(verbose_name="Altura en M")
    peso = models.FloatField(verbose_name="Peso en KG")
    BINARIO = (
        (1,'Si'),
        (0,'No'),
    )
    historial_obesidad = models.IntegerField(choices=BINARIO, verbose_name="Historial de sobrepeso en su familia")
    favc = models.IntegerField(choices=BINARIO, verbose_name="Come frecuentemente alimentos con altos niveles calóricos")
    VEGETALES = (
        (1,'Nunca'),
        (2,'Algunas veces'),
        (3,'Siempre'),
    )
    fcvc = models.IntegerField(choices=VEGETALES, verbose_name="Come vegetales en sus comidas")
    COMIDAS = (
        (1,'Entre 1 y 2'),
        (2,'Tres'),
        (3,'Más de tres'),
    )
    npc = models.IntegerField(choices=COMIDAS, verbose_name="Número de comidas principales al día")
    ALIMENTOS = (
        (1,'No'),
        (2,'Algunas veces'),
        (3,'Frecuentemente'),
        (4,'Siempre')
    )
    caec = models.IntegerField(choices=ALIMENTOS, verbose_name="Come algún alimento entre comidas")
    BINARIO = (
        (0,'No'),
        (1,'Si'),
    )
    smoke = models.IntegerField(choices=BINARIO, verbose_name="¿Fuma?")
    AGUA = (
        (1,'Menos de un litro'),
        (2,'Entre 1 y 2 litros'),
        (3,'Más de 2 litros')
    )
    ch2o = models.IntegerField(choices=AGUA, verbose_name="Consumo de agua diario")
    scc = models.IntegerField(choices=BINARIO, verbose_name="Monitorea el número de calorías que consume diario")
    ACTIVIDAD = (
        (0,'No practica'),
        (1,'1 a 2 días por semana'),
        (2,'2 a 4 días por semana'),
        (3,'3 a 5 días por semana'),
    )
    faf = models.IntegerField(choices=ACTIVIDAD, verbose_name="Frecuencia con la que practica actividad física")
    DISPOSITIVOS = (
        (0,'0 a 2 horas al día'),
        (1,'3 a 5 horas al día'),
        (2,'Más de 5 horas al día'),
    )
    tue = models.IntegerField(choices=DISPOSITIVOS, verbose_name="Tiempo que usa dispositivos electrónicos al día")
    ALCOHOL = (
        (1,'No'),
        (2,'Algunas veces'),
        (3,'Frecuentemente'),
        (4,'Siempre')
    )
    calc = models.IntegerField(choices=ALCOHOL, verbose_name="Tiempo que usa dispositivos electrónicos al día")
    TRANSPORTE = (
        (1,'Automóvil'),
        (2,'Motocicleta'),
        (3,'Bicicleta'),
        (4,'Transporte público'),
        (5,'Caminar')
    )
    mtrans = models.IntegerField(choices=TRANSPORTE, verbose_name="Medio de transporte principal")
    OBESIDAD = (
        (1,'Peso insuficiente'),
        (2,'Peso normal'),
        (3,'Sobrepeso nivel 1'),
        (4,'Sobrepeso nivel 2'),
        (5,'Obesidad tipo 1'),
        (6,'Obesidad tipo 2'),
        (7,'Obesidad tipo 3')
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de diagnóstico")
    nobeyesdad = models.IntegerField(choices=OBESIDAD, verbose_name="Peso corporal")

    class Meta:
        ordering = ('-idUsuario',)

    def __str__(self):
        return '{0}'.format(self.idUsuario.username)
    
