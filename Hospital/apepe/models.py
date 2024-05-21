from django.db import models

# Create your models here.
from datetime import datetime
from typing import List, Optional

from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Doctor(Persona):
    especialidades = models.ManyToManyField(Especialidad, related_name='doctores')

class Enfermero(models.Model):
    num_enfermero = models.IntegerField(unique=True)
    doctores = models.ManyToManyField(Doctor, related_name='enfermeros')

    def __str__(self):
        return str(self.num_enfermero)

class Paciente(Persona):
    expediente_medico = models.OneToOneField('ExpedienteMedico', on_delete=models.SET_NULL, null=True, blank=True)

class ExpedienteMedico(models.Model):
    historial_medico = models.TextField()

    def __str__(self):
        return self.historial_medico

class CitasMedicas(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=255)
    estado = models.CharField(max_length=50)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fecha} {self.hora} - {self.motivo}'
