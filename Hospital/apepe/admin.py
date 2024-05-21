from django.contrib import admin
from .models import Doctor, Paciente, Enfermero, CitasMedicas, ExpedienteMedico

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dni', 'direccion')
    search_fields = ('nombre', 'dni')
    filter_horizontal = ('especialidades',)
    list_filter = ('especialidades',)

@admin.register(Enfermero)
class EnfermeroAdmin(admin.ModelAdmin):
    list_display = ('num_enfermero',)
    search_fields = ('num_enfermero',)
    filter_horizontal = ('doctores',)

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dni', 'direccion')
    search_fields = ('nombre', 'dni')

@admin.register(CitasMedicas)
class CitasMedicasAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'hora', 'motivo', 'estado', 'paciente', 'doctor')
    search_fields = ('motivo', 'estado', 'paciente__nombre', 'doctor__nombre')
    list_filter = ('fecha', 'estado', 'doctor', 'paciente')

@admin.register(ExpedienteMedico)
class ExpedienteMedicoAdmin(admin.ModelAdmin):
    list_display = ('historial_medico',)
    search_fields = ('historial_medico',)
    list_filter = ('historial_medico',)
