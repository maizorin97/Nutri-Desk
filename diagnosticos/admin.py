from django.contrib import admin

from .models import Diagnostico

# Register your models here.
class DiagnosticoAdmin(admin.ModelAdmin):
    readonly_fields = ()
    list_display = ('idDiagnostico','idUsuario','fecha_creacion')

admin.site.register(Diagnostico, DiagnosticoAdmin)