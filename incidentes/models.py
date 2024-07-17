from django.db import models

class Incidentes(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    status = models.CharField(max_length=50)
    local = models.CharField(max_length=100)
    data_hora = models.DateTimeField()
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    acoes = models.TextField()

    def __str__(self):
        return self.titulo
