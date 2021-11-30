from django.db import models
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

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

class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, related_name="comentarios", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    body = models.TextField()
    fecha= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.articulo.titulo, self.nombre)
    
