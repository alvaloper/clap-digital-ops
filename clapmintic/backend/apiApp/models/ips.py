from django.db import models

class Ips(models.Model):
    id_reps = models.CharField(primary_key=True, max_length=255)
    nombre = models.CharField(max_length=255)
    tipo_de_entidad = models.CharField(max_length=255)
    representante = models.CharField(max_length=255)
    nivel_de_atencion = models.CharField(max_length=255)
