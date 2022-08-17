from django.core import exceptions
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth.models import User
from SuiteApp.models import *



class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )

        return user

    class Meta:
        model = User
        fields = ("id", "username", "password", "email")

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        exclude = ('user_permissions', 'is_staff', 'is_superuser', 'is_active')

class ReadUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('user_permissions', 'password', 'is_staff', 'is_superuser', 'is_active')

class ReadDetailUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('user_permissions', 'password', 'is_staff', 'is_superuser', 'is_active')
        depth = 4

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        data['user'] = {}
        data['user']['id'] = user.id
        data['user']['username'] = user.username
        data['user']['first_name'] = user.first_name
        data['user']['last_name'] = user.last_name
        data['user']['email'] = user.email
        data['user']['is_active'] = user.is_active
        data['user']['date_joined'] = user.date_joined
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

