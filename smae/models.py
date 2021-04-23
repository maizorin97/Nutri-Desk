from django.db import models

class Grupo(models.Model):
    idGrupo = models.IntegerField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50)
    subgrupo = models.CharField(null=True, blank=True, max_length=50)
    energia = models.IntegerField(verbose_name="Energía (kcal)")
    proteina = models.IntegerField(verbose_name="Proteína (g)")
    lipidos = models.IntegerField(verbose_name="Lípidos (g)")
    carbohidratos = models.IntegerField(verbose_name="Hidratos de Carbono (g)")

    class Meta:
        ordering = ('idGrupo',)

    def __str__(self):
        id_grupo = self.idGrupo
        nom = self.nombre
        subg = self.subgrupo
        if (subg is "None"):
            subg = ""
        return '{0} - {1} {2}'.format(self.idGrupo, self.nombre, self.subgrupo)


class Alimento(models.Model):
    idAlimento = models.AutoField(primary_key=True)
    idGrupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    racion = models.CharField(max_length=50)

    class Meta:
        ordering = ('idAlimento',)

    def __str__(self):
        return 'id:{0} - {1}'.format(self.idAlimento, self.nombre)

# inserciones de datos mediante codigo
# grupo = Grupo.objects.get(idGrupo=1)
# b2 = Alimento(idGrupo=grupo, nombre='gg',racion='gg*2')
# b2.save()