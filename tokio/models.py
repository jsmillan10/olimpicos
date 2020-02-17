from django.db import models
from django.utils import timezone

# Create your models here.

class Deportes(models.Model):
    nombre = models.CharField(max_length=60, null=True)
    foto = models.ImageField(upload_to='images/deportes', null=True)

    def __str__(self):
        return self.nombre

class Entrenadores(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)

    def __str__(self):
        return self.nombres + ' ' + self.apellidos

class Deportistas(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    lugarNac = models.CharField(max_length=100)
    fechaNac = models.DateField()
    edad = models.IntegerField()
    peso = models.FloatField()
    estatura = models.FloatField()
    foto = models.ImageField(upload_to='images/deportistas')
    entrenador = models.ForeignKey(Entrenadores, on_delete=models.CASCADE, db_column='id_entrenador', null=True)

    def __str__(self):
        return self.nombres + ' ' + self.apellidos


class DeportesDeportistas(models.Model):
    deportista = models.ForeignKey(Deportistas, on_delete=models.CASCADE, db_column='id_deportistas', null=True)
    deporte = models.ForeignKey(Deportes, on_delete=models.CASCADE, db_column='id_deporte', null=True)

class Estudiante(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombres + ' ' + self.apellidos

class Participaciones(models.Model):
    deporte = models.ForeignKey(Deportes, models.CASCADE, db_column='id_deporte', null=True)
    modalidad = models.CharField(max_length=100)
    linkVideo = models.CharField(max_length=100)
    fecha = models.DateField(default=timezone.now)
    hora = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.deporte.__str__() + ' ' + self.modalidad.__str__() + ' ' + self.fecha.__str__() + ' ' + self.hora.__str__()


class Comentarios(models.Model):
    participacion = models.ForeignKey(Participaciones, on_delete=models.CASCADE, db_column='id_participacion', null=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, db_column='id_estudiante', null=True)
    fechaCreacion = models.DateField(default=timezone.now)
    comentario = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.comentario.__str__()