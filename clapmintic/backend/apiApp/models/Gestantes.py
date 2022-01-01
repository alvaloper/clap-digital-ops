from django.db import models
    
class Gestantes(models.Model):
    id_gestantes = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    fecha_registro = models.DateField(auto_now=True)
    tipo_de_entidad = models.CharField(max_length=100)
    id_REPS = models.IntegerField(foreign_key=True)
    id_departamentos = models.IntegerField(foreign_key=True)
    id_municipios = models.IntegerField(foreign_key=True)
    regimen_aplicacion = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    id_etnia = models.IntegerField(foreign_key=True)
    