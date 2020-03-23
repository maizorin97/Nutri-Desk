from django.shortcuts import render, redirect

from django.views.generic import CreateView, ListView, TemplateView

from .models import Plan

class lista_planes(ListView):
    template_name = "lista_planes.html"
    model = Plan
    context_object_name = 'lista_planes'

def generar_planes(request):
    if request.method == 'POST':
        guardar_plan(request.POST)
        return redirect("ingresar")
        #valida
        """if user_form.is_valid() and info_form.is_valid():
            user = user_form.save()
            info = info_form.save(commit=False)
            info.usuario = user
            info.save()
            # exito
            return redirect("ingresar")
        else:
            return render(request, "registro.html",{'user_form':user_form,'info_form':info_form})"""
    else:
        return preparar_plan(request.user, request)


def preparar_plan(current_user, request):
    from core.models import InfoUsuario
    from smae.models import Alimento, Grupo
    from datetime import datetime as dt
    
    #filter(usuario=current_user)#.all()
    infoUser = InfoUsuario.objects.get(usuario=current_user)
    listaGrupos = Grupo.objects.all()
    listaAlimentos = Alimento.objects.all()
    edad = dt.now().year - infoUser.fecha_nacimiento.year + (dt.now().month - infoUser.fecha_nacimiento.month)*(1/12)

    return render(request,'generar_plan.html',{'infoUser':infoUser,'edad':edad,'listaAlimentos':listaAlimentos,'listaGrupos':listaGrupos})


def guardar_plan(req_post):
    nombre_plan = req_post.get("txtNombrePlan")
    aporte_kcal = int(req_post.get("txtAporteCalorico"))
    print("nombre=" + nombre_plan + " kcal=" + str(aporte_kcal))
    llave_comida = ("Desayuno","Colacion1","Comida","Colacion2","Cena")
    comidas = []
    for comida in llave_comida:
        comidas.append(req_post.getlist(comida))
    print(str(comidas))