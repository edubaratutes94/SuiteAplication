import datetime
import uuid
import os
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.db import models
from django.conf import settings
from django.db.models.signals import *
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from SuiteApp.utils import *

class UserApp(User):
    uui = models.UUIDField(default=uuid.uuid4, editable=False, null=True)
    image = models.ImageField(upload_to='static/users', verbose_name="Avatar",
                              null=True, default='static/users/userDefault1.png')
    referUser = models.UUIDField(null=True)
    fa2 = models.BooleanField(verbose_name="2FA", default=False)

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
    telefono_particular = models.CharField(max_length=10, validators=[validate_only_numbers])
    telefono_celular = models.CharField(max_length=8, validators=[validate_only_numbers])

    def __str__(self):
        return self.usuario.username

    def crearUsuario(sender, instance, created, **kwargs):
        if created:
            registrarUsuario.objects.create(usuario=instance)

    def guardarUsuario(sender, instance, **kwargs):
        instance.registrarusuario.save()