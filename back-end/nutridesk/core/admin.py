from django.contrib import admin
from .models import InfoUsuario

# Register your models here.
class CoreAdmin(admin.ModelAdmin):
    readonly_fields = ()
    list_display = ()

admin.site.register(InfoUsuario, CoreAdmin)
