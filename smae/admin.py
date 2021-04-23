from django.contrib import admin
from .models import Grupo, Alimento

class GrupoAdmin(admin.ModelAdmin):
    readonly_fields = ()
    list_display = ('idGrupo','nombre','subgrupo','energia','proteina','lipidos','carbohidratos')

admin.site.register(Grupo, GrupoAdmin)

class AlimentoAdmin(admin.ModelAdmin):
    readonly_fields = ()
    list_display = ('idAlimento','idGrupo','nombre','racion')

admin.site.register(Alimento, AlimentoAdmin)

