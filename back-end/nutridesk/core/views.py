from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy
from datetime import timedelta
from django.utils import timezone

from . import models, forms


class index(TemplateView):
    template_name = "index.html"

class ingresar(LoginView):
    template_name = "ingresar.html"
    form_class = forms.FormaInicioSesion
    success_url = "/index"

    def get_success_url(self):
        return super().get_success_url()

class registro(CreateView):
    template_name = "registro.html"
    form_class = forms.FormaRegistroUsuario
    success_url = "/ingresar"

    def get_success_url(self):
        return super().get_success_url()

class cerrar(LogoutView):
    template_name = "cerrar.html"


class error(TemplateView):
    template_name = "error.html"
