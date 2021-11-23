from django.contrib import admin
from .models import InfoUsuario, PesosUsuario, CalendarioUsuario, BitacoraUsuario

# Register your models here.
class CoreAdmin(admin.ModelAdmin):
    readonly_fields = ()
    list_display = ('usuario','peso','altura','fecha_nacimiento','sexo')
admin.site.register(InfoUsuario, CoreAdmin)

class PesosUsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ()
    list_display = ('idPeso','usuario','fecha_creacion','peso')
admin.site.register(PesosUsuario, PesosUsuarioAdmin)

class CalendarioUsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ()
    list_display = ('idCalendario','usuario')
admin.site.register(CalendarioUsuario, CalendarioUsuarioAdmin)

class BitacoraUsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ()
    list_display = ('idBitacora','usuario','fecha_registro', 'estado_animo')
admin.site.register(BitacoraUsuario, BitacoraUsuarioAdmin)