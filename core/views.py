from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView

from core.models import InfoUsuario, PesosUsuario

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


def registro(request):
    if request.method == 'POST':
        user_form = forms.FormaRegistroUsuario(request.POST)
        info_form = forms.FormaDatosFisiologicos(request.POST)
        if user_form.is_valid() and info_form.is_valid():
            user = user_form.save()
            info = info_form.save(commit=False)
            info.usuario = user
            info.save()
            # Esto solo es para ir guardando un historial de pesos del usuario
            info_user = get_object_or_404(InfoUsuario, usuario=request.user)
            pesos_history = PesosUsuario(
                usuario=info_user.usuario, peso=info_user.peso)
            pesos_history.save()
            ##################################################################
            # exito
            return redirect("ingresar")
        else:
            return render(request, "registro.html", {'user_form': user_form, 'info_form': info_form})
    else:
        user_form = forms.FormaRegistroUsuario()
        info_form = forms.FormaDatosFisiologicos()
        return render(request, 'registro.html', {'user_form': user_form, 'info_form': info_form})


def panel_control(request):
    infoUser = InfoUsuario.objects.get(usuario=request.user)
    pesosUser = PesosUsuario.objects.filter(usuario=request.user)
    print(PesosUsuario)
    return render(request, 'panel_control.html', {'infoUser': infoUser, 'pesosUser': pesosUser})


#path('perfil/<int:id>/', views.perfil, name='perfil'),
# def perfil(request,id):

def perfil(request):
    if request.method == "POST":
        info_user = get_object_or_404(InfoUsuario, usuario=request.user)
        info_form = forms.FormaDatosFisiologicos(
            request.POST or None, instance=info_user)
        print("intentando guardar")
        print(info_form.errors)
        if info_form.is_valid():
            print("se pudo")
            info_form.save()
            # Esto solo es para ir guardando un historial de pesos del usuario
            info_user = get_object_or_404(InfoUsuario, usuario=request.user)
            pesos_history = PesosUsuario(
                usuario=info_user.usuario, peso=info_user.peso)
            pesos_history.save()
            ##################################################################
            return redirect('perfil')
        else:
            print("no se pudo")
            return render(request, "perfil.html", {'info_form': info_form})
    else:
        info_user = get_object_or_404(InfoUsuario, usuario=request.user)
        info_form = forms.FormaDatosFisiologicos(instance=info_user)

        return render(request, "perfil.html", {'info_form': info_form})


class cerrar(LogoutView):
    template_name = "cerrar.html"


class error(TemplateView):
    template_name = "error.html"
