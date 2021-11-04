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





# Nomencladores
class TipoViviendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_vivienda
        fields = ('uui', 'tipo')


class TipoAlojamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_alojamiento
        fields = ('uui', 'tipo')

class TipoCamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_cama
        fields = ('uui', 'tipo')

class TipoAlimentacion(serializers.ModelSerializer):
    class Meta:
        model = Tipo_alimentacion
        fields = ('uui', 'tipo')


class HabitacionSerializer(serializers.ModelSerializer):
    tipo_cama = serializers.SerializerMethodField()
    class Meta:
        model = Habitacion
        fields = ('uui', 'nombre', 'banno_privado', 'tipo_cama')

    def get_tipo_cama(self, obj):
        return obj.tipo_cama.uui

# NOMENCLADORES Listado----------------------------------------------------------------------------

class RegistroViviendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrovivienda
        fields = '__all__'




# class MunicipalitySerializer(serializers.ModelSerializer):
#     province = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Municipality
#         fields = ('uui', 'name', 'province')
#
#     def get_province(self, obj):
#         return obj.province.uui