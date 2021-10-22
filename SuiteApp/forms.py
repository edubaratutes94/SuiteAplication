from django import forms
from django.contrib.admin.utils import help_text_for_field
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from SuiteApp.models import *
from django.forms import TextInput, NumberInput, Select, Textarea, CheckboxSelectMultiple, DateTimeInput, SelectDateWidget, \
    CheckboxInput, PasswordInput, EmailInput, DateInput, IntegerField

class registrarForm(UserCreationForm):

    class Meta:
        model = registrarUsuario
        fields = [
            'first_name',
            'last_name',
            'email',
            'direccion',
            'fecha_nacimiento',
            'rol',
            'telefono_particular',
            'telefono_celular',
            'username',
            'password1',
            'password2',
        ]
        widgets = {

            'username': TextInput(),
            'email': EmailInput(),
            'first_name': TextInput(),
            'last_name': TextInput(),
            'direccion': TextInput(),
            'fecha_nacimiento': DateInput(),
            'telefono_particular': TextInput(),
            'telefono_celular': TextInput,
            'password1': PasswordInput(),
            'password2': PasswordInput(),
        }

        labels = {
            'username': 'Nombre de usuario',
            'email': 'Direccion de correo electrónico',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'direccion': 'Dirección particular',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'rol': 'Rol',
            'telefono_particular': 'Teléfono particular',
            'telefono_celular': 'Teléfono celular',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        help_text = {

            'fecha_nacimiento': 'AA-MM-DD',
        }

class FormularioTipoUser(forms.ModelForm):
    class Meta:
        model = tblRol
        fields = ['rol']
        widgets = {

            'rol': TextInput(attrs={'class': 'form-control tooltips'}),
        }
        labels = {
            'rol': 'Rol de Usuario',
        }