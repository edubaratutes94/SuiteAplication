from django.core import exceptions
from django.contrib.auth import authenticate
from rest_framework import serializers
from SuiteApp.models import *

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = {"msg": "Usuario desactivado"}
                    raise exceptions.ValidationError(msg)
            else:
                user = User.objects.filter(username=username)
                if user.count() > 0:
                    if not user.get().is_active:
                        msg = {"msg": "Usuario pendiente de activación"}
                        raise exceptions.ValidationError(msg)
                    else:
                        msg = {"msg": "Error en el login, credenciales erroneas."}
                        raise exceptions.ValidationError(msg)
                else:
                    msg = {"msg": "Error en el login, credenciales erroneas."}
                    raise exceptions.ValidationError(msg)
        else:
            msg = {"msg": "Debe escribir usuario o contraseña, los dos!"}
            raise exceptions.ValidationError(msg)
        return data
