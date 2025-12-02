from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tecnologia = models.CharField(max_length=200)
    enlace = models.URLField()
    imagen = models.ImageField(upload_to='proyectos/')

    def __str__(self):
        return self.titulo


