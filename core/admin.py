from django.contrib import admin
from .models import InfoUsuario, PesosUsuario

# Register your models here.
class CoreAdmin(admin.ModelAdmin):
    readonly_fields = ()
    list_display = ('usuario','peso','altura','fecha_nacimiento','sexo')

class PesosUsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ()
    list_display = ('idPeso','usuario','fecha_creacion','peso')

admin.site.register(InfoUsuario, CoreAdmin)
admin.site.register(PesosUsuario, PesosUsuarioAdmin)
