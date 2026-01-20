from django.contrib import admin
from .models import Vehiculo

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'marca', 'modelo', 'usuario')  # Campos mostrados en la lista del admin
    search_fields = ('matricula', 'marca', 'modelo')  # Habilita búsqueda por estos campos

admin.site.register(Vehiculo, VehiculoAdmin)