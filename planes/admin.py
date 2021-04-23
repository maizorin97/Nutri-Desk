from django.contrib import admin
from .models import Plan, Colacion, TipoComida

class PlanAdmin(admin.ModelAdmin):
    readonly_fields = ()
    list_display = ('idPlan','idUsuario','descripcion','calorias')
admin.site.register(Plan, PlanAdmin)

class ColacionAdmin(admin.ModelAdmin):
    readonly_fields = ()
    list_display = ('idColacion','idPlan','idAlimento','idTipoComida')
admin.site.register(Colacion, ColacionAdmin)

class TipoComidaAdmin(admin.ModelAdmin):
    readonly_fields = ()
    list_display = ('idTipoComida','nombre')
admin.site.register(TipoComida, TipoComidaAdmin)

