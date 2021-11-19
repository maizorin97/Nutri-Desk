from django.contrib import admin

from .models import DiagnosticoCardio, DiagnosticoObesidad

# Register your models here.
class DiagnosticoCardioAdmin(admin.ModelAdmin):
    readonly_fields = ()
    list_display = ('idDiagnostico','idUsuario','fecha_creacion')
admin.site.register(DiagnosticoCardio, DiagnosticoCardioAdmin)

class DiagnosticoObesidadAdmin(admin.ModelAdmin):
    readonly_fields = ()
    list_display = ('idDiagnostico','idUsuario','fecha_creacion')
admin.site.register(DiagnosticoObesidad, DiagnosticoObesidadAdmin)