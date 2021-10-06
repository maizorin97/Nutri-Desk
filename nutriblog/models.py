from django.db import models
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.


class Articulo(models.Model):
    titulo = models.CharField(max_length=128)
    autor = models.CharField(max_length=128)
    cuerpo = RichTextField(blank="True", null="True")
    fecha = models.DateField(auto_now_add=True)
    abstract = models.CharField(max_length=120, default="Resumen del articulo")
    portada = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self) -> str:
        return self.titulo+' | '+self.autor
