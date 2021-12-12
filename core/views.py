from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView

from core.models import InfoUsuario, PesosUsuario, CalendarioUsuario, BitacoraUsuario
from smae.models import Alimento

from django.urls import reverse_lazy
from datetime import datetime, timedelta, date
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
            # Guardar historial de pesos del usuario
            info_user = get_object_or_404(InfoUsuario, usuario=user)
            pesos_history = PesosUsuario(usuario=info_user.usuario, peso=info_user.peso)
            pesos_history.save()
            # Inicializar calendario vacio para planes
            calendario = CalendarioUsuario(usuario=info_user.usuario)
            calendario.save()
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
    pesosUser = PesosUsuario.objects.filter(usuario=request.user).values('peso')
    fechasPeso = PesosUsuario.objects.filter(usuario=request.user).values('fecha_creacion')
    labels=[]
    data=[]
    fecha_actual= datetime.now()
    existe_bitacora_hoy = BitacoraUsuario.objects.filter(usuario=request.user).filter(fecha_registro=datetime.now()).count() > 0
    exise_plan_hoy = CalendarioUsuario.objects.filter(usuario=request.user).count() > 0

    bitacoras_sentimiento = BitacoraUsuario.objects.filter(usuario = request.user)
    bitacoras_mes = []
   

    print(bitacoras_sentimiento)

    for x in bitacoras_sentimiento:
        if x.fecha_registro.month == datetime.now().month:
            bitacoras_mes.append(x)

    plan_hoy = None
    if exise_plan_hoy:
        week_day_now = fecha_actual.weekday()
        #plan_hoy = CalendarioUsuario.objects.get(usuario=request.user)._meta.get_field(week_day_map[week_day_now])
        plan_hoy = CalendarioUsuario.objects.get(usuario=request.user)

        if(week_day_now == 0):
            plan_hoy = plan_hoy.planLunes
        elif(week_day_now == 1):
            plan_hoy = plan_hoy.planMartes
        elif(week_day_now == 2):
            plan_hoy = plan_hoy.planMiercoles
        elif(week_day_now == 3):
            plan_hoy = plan_hoy.planJueves
        elif(week_day_now == 4):
            plan_hoy = plan_hoy.planViernes
        elif(week_day_now == 5):
            plan_hoy = plan_hoy.planSabado
        elif(week_day_now == 6):
            plan_hoy = plan_hoy.planDomingo

    for peso in pesosUser:
        data.append(peso['peso'])

    for fecha in fechasPeso:
        labels.append(fecha['fecha_creacion'].isoformat())
    
    if request.method == "POST":
        
        nuevo_registro = BitacoraUsuario(
            usuario = request.user,
            comentario = None if request.POST.get("txtComentario") == '' else request.POST.get("txtComentario"),
            estado_animo = request.POST.get("sentimientos"),
            agua = 1 if request.POST.get("agua") == 'on' else 0,
            ejercicio = 1 if request.POST.get("run") == 'on' else 0,
            buen_suenio = 1 if request.POST.get("cama") == 'on' else 0,
            comer_sano = 1 if request.POST.get("manzana") == 'on' else 0,
        ).save()

        existe_bitacora_hoy = True


    return render(request, 'panel_control.html', {
        'infoUser': infoUser, 
        'pesosUser': pesosUser,
        'data': data,
        'labels' : labels,
        'fecha': fecha_actual,
        'existe_bitacora_hoy': existe_bitacora_hoy,
        'plan_hoy': plan_hoy,
        'bitacoras': bitacoras_mes
    })


def perfil(request):
    if request.method == "POST":
        info_user = get_object_or_404(InfoUsuario, usuario=request.user)
        info_form = forms.FormaDatosFisiologicos(
            request.POST or None, request.FILES, instance=info_user)
        print("intentando guardar")
        print(info_form.errors)
        if info_form.is_valid():
            print("se pudo")
            info_form.save()
            print(info_form.cleaned_data)
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
        
        return render(request, "perfil.html", {'info_form': info_form,'infoUser':info_user})

class contacto(TemplateView):
    template_name = "contacto.html"

class cerrar(LogoutView):
    template_name = "cerrar.html"


class error(TemplateView):
    template_name = "error.html"
