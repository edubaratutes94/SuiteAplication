
# Create your views here.

from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView, ListView
from rest_framework.reverse import reverse_lazy
from django.contrib.messages.api import success, error
from django.contrib.admin.models import ADDITION, CHANGE

from SuiteApp.models import *
from SuiteApp.forms import *

# Nomencladores




# Create your views here.
class registrarView(CreateView):
    model = registrarUsuario
    form_class = registrarForm

    def form_valid(self, form):
        form.is_staff = True
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/api/v1/login')


class insertarTipoUser(RequiredSecurityMixin, SuccessMessageMixin, CreateView):
    need_login = True
    permission = RequiredSecurityMixin.CREATE
    model = tblRol
    template_name = 'SuiteApp/rol.html'
    form_class = FormularioTipoUser
    success_url = '/registrar'


    def get_context_data(self, **kwargs):
        context = super(insertarTipoUser, self).get_context_data(**kwargs)

        return context

    def form_invalid(self, form):
        error(self.request, 'Por favor corrija los errores.')
        return super(insertarTipoUser, self).form_invalid(form)

    def get_success_url(self):
        register_logs(self.request, self.model, self.object.pk, force_str(self.object), ADDITION)
        return super(insertarTipoUser, self).get_success_url()

class logOut(LogoutView):
    pass