from django.contrib import admin
from SuiteApp import models
# Register your models here.
admin.site.register(models.UserApp)
admin.site.register(models.Tipo_vivienda)
admin.site.register(models.Tipo_cama)
admin.site.register(models.Habitacion)
admin.site.register(models.Tipo_alojamiento)
admin.site.register(models.Tipo_alimentacion)
admin.site.register(models.Registrovivienda)