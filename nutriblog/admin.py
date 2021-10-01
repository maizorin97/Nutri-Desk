from django.contrib import admin

# Register your models here.
from .models import Articulo

# Register your models here.


class articuloAdmin(admin.ModelAdmin):
    readonly_fields = ()
    list_display = ('titulo', 'autor', 'cuerpo',
                    'fecha', 'abstract', 'portada')


admin.site.register(Articulo, articuloAdmin)
