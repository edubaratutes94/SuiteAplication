import datetime
import uuid
import os
import datetime
import uuid
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.db import models
from django.conf import settings
from django.db.models.signals import *
from rest_framework.authtoken.models import Token
from django.dispatch import receiver


class UserApp(User):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uui = models.UUIDField(default=uuid.uuid4, editable=False, null=True)
    image = models.ImageField(upload_to='static/users', verbose_name="Avatar",
                              null=True, default='static/users/userDefault1.png')

    def __str__(self):
        return str(self.username)

    def Online(self):
        for s in Session.objects.all():
            if s.get_decoded():
                if self.id == int(s.get_decoded()['_auth_user_id']):
                    now = datetime.datetime.now()
                    dif = (now - s.expire_date)
                    if dif < datetime.timedelta(seconds=0):
                        return True
        return False

    class Meta:
        verbose_name_plural = "Usuarios"


class tblRol(models.Model):

    rol= models.CharField(max_length=25, unique=True, null=False, primary_key=True)

    def __str__(self):
        return self.rol


class registrarUsuario(User):
    usuario = models.OneToOneField(User, null=False, on_delete=models.CASCADE, parent_link=True)
    rol = models.ForeignKey(tblRol, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(editable=True)
    direccion = models.TextField(max_length=150)
    telefono_particular = models.IntegerField()
    telefono_celular = models.IntegerField()

    def __str__(self):
        return self.usuario.username

    def crearUsuario(sender, instance, created, **kwargs):
        if created:
            registrarUsuario.objects.create(usuario=instance)

    def guardarUsuario(sender, instance, **kwargs):
        instance.registrarusuario.save()

# class User con los datos
#     nombre_apellidos = models.CharField(max_length=50)
#     ci = models.IntegerField()
#     fecha_nacimiento = models.DateField()
#     sexo = models.CharField()
#     direccion = models.CharField()
#     correo = models.EmailField()
#     telefono = models.IntegerField()
#     idioma = models.CharField()
#     ubicacion = models.CharField()
#     tarjeta_credito = models.CharField()

class Tipo_vivienda(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uui = models.UUIDField(default=uuid.uuid4, editable=False)
    tipo = models.CharField(max_length=100)  # departamento, casa, vivienda anexa, alojamiento unico, etc...

    def __str__(self):
        return self.tipo


class Tipo_alojamiento(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uui = models.UUIDField(default=uuid.uuid4, editable=False)
    tipo = models.CharField(max_length=100)  # alojaminto entero, habitacion privada, habitacion compartida

    def __str__(self):
        return self.tipo


class Tipo_cama(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uui = models.UUIDField(default=uuid.uuid4, editable=False)
    tipo = models.CharField(max_length=100)  # king, queen, pesonal, litera

    def __str__(self):
        return self.tipo

class Tipo_alimentacion(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uui = models.UUIDField(default=uuid.uuid4, editable=False)
    tipo = models.CharField(max_length=100)  # desayuno, cena, almuerzo

    def __str__(self):
        return self.tipo


class Habitacion(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uui = models.UUIDField(default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    banno_privado = models.BooleanField(blank=True, null=True)
    tipo_cama = models.ForeignKey(Tipo_cama, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Registrovivienda(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uui = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserApp, on_delete=models.CASCADE)
    licencia = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    # ubicacion_geografica
    codigo_postal = models.IntegerField()
    # Perfil de la propiedad y especificaciones
    nombre = models.CharField(max_length=100)
    tipo_vivienda = models.ForeignKey(Tipo_vivienda, on_delete=models.CASCADE)
    descripcion_tipo_vivienda = models.TextField(max_length=500, blank=True, null=True)
    tipo_alojamiento = models.ForeignKey(Tipo_alojamiento, on_delete=models.CASCADE)
    dimensiones = models.DecimalField(max_digits=3, decimal_places=2)
    cant_huespedes = models.IntegerField()
    cant_habitaciones = models.IntegerField()
    habitaciones = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    cant_camas_por_habitaciones = models.IntegerField()
    #  combinaciones_camas = models.CharField(max_length=100)
    cant_bannos = models.IntegerField()
    imagen = models.ImageField(upload_to='static/home', verbose_name="Home", null=True,
                               default='static/home/homeDefault.png')
    # No se q poner
    hora_check_in = models.DateField()
    hora_check_out = models.DateField()
    fecha_inicio_disponibilidad = models.DateField()  # consultar
    decoracion_iluminacion = models.TextField(blank=True, null=True)
    # Precios
    por_una_noche = models.DecimalField(max_digits=8, decimal_places=2)
    por_noche_siete = models.DecimalField(max_digits=8, decimal_places=2)
    por_noche_treinta = models.DecimalField(max_digits=8, decimal_places=2)
    por_fin_semana = models.DecimalField(max_digits=8, decimal_places=2)
    # Servicios
    toalla_sabanas = models.BooleanField(blank=True, null=True)
    papel_higienico = models.BooleanField(blank=True, null=True)
    tv_habitacion = models.BooleanField(blank=True, null=True)
    aire_acondicionado = models.BooleanField(blank=True, null=True)
    ventilador = models.BooleanField(blank=True, null=True)
    caja_fuerte = models.BooleanField(blank=True, null=True)
    perchas = models.BooleanField(blank=True, null=True)
    banno_privado = models.BooleanField(blank=True, null=True)
    aguafria_caliente = models.BooleanField(blank=True, null=True)
    # Mas informacion
    ascensor = models.BooleanField(blank=True, null=True)
    ascensor_discapacitados = models.BooleanField(blank=True, null=True)
    permitido_fumar = models.BooleanField(blank=True, null=True)
    sombrilla = models.BooleanField(blank=True, null=True)
    piscina = models.BooleanField(blank=True, null=True)
    jacuzzi = models.BooleanField(blank=True, null=True)
    gimnasio = models.BooleanField(blank=True, null=True)
    ranchon = models.BooleanField(blank=True, null=True)
    terraza = models.BooleanField(blank=True, null=True)
    jardin_patio = models.BooleanField(blank=True, null=True)
    mascotas = models.BooleanField(blank=True, null=True)
    portero = models.BooleanField(blank=True, null=True)
    cocina = models.BooleanField(blank=True, null=True)
    alimentacion = models.BooleanField(blank=True, null=True)  # Desayuno, Almuerzo, Cena
    refrigerador_minibar = models.BooleanField(blank=True, null=True)
    tv = models.BooleanField(blank=True, null=True)
    calentador_agua = models.BooleanField(blank=True, null=True)
    lavadora = models.BooleanField(blank=True, null=True)
    secadora = models.BooleanField(blank=True, null=True)
    apto_familiar = models.BooleanField(blank=True, null=True)
    garage = models.BooleanField(blank=True, null=True)
    secador_pelo = models.BooleanField(blank=True, null=True)
    plancha = models.BooleanField(blank=True, null=True)
    entrada_independiente = models.BooleanField(blank=True, null=True)
    impresora = models.BooleanField(blank=True, null=True)
    telefono = models.BooleanField(blank=True, null=True)
    wifi = models.BooleanField(blank=True, null=True)
    internet = models.BooleanField(blank=True, null=True)
    # Descripcion localidad
    movilidad_turista_casa = models.TextField(blank=True, null=True)
    lugares_cercanos = models.TextField(blank=True, null=True)
    alrededores_casa = models.TextField(blank=True, null=True)
    movilidad_turista_calle = models.TextField(blank=True, null=True)
    redes_sociales = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Transporte(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uui = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserApp, on_delete=models.CASCADE)
    marca = models.CharField(max_length=100)

    # licencia = models.CharField()
    # tarjeta_credito = models.CharField() #ver si el campo es char o integer

    def __str__(self):
        return self.marca


class Guia_Turistica(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uui = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserApp, on_delete=models.CASCADE)

    # licencia = models.CharField(max_length=100)
    # tarjeta_credito = models.CharField(max_length=100) #ver si el campo es char o integer

    def __str__(self):
        return self.user.first_name


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

    for user in User.objects.all():
        Token.objects.get_or_create(user=user)
