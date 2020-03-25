from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic import CreateView, ListView, TemplateView

from .models import Plan, TipoComida, Colacion
from core.models import InfoUsuario
from smae.models import Alimento, Grupo
from django.contrib.auth.models import User

from datetime import datetime as dt


class lista_planes(ListView):
    template_name = "lista_planes.html"
    model = Plan
    context_object_name = "lista_planes"


def generar_planes(request):
    if request.method == "POST":
        usuario: User = InfoUsuario.objects.get(usuario=request.user).usuario
        guardar_plan(request.POST, usuario)
        return redirect("planes")
    else:
        return preparar_plan(request.user, request)


def ver_plan(request, plan_id):
    if request.method == "POST":
        pass
    else:
        plan = Plan.objects.get(idPlan=plan_id)
        colaciones = Colacion.objects.filter(idPlan=plan)
        tipos_comidas = TipoComida.objects.all()
        return render(request, "ver_plan.html", {"plan": plan,"colaciones":colaciones,"tipos_comidas":tipos_comidas})

def eliminar_plan(request, plan_id):
    context = {}
    obj_plan = get_object_or_404(Plan, idPlan=plan_id)

    if request.method == "POST":
        obj_plan.delete()
        return redirect("planes")
    else:
        return render(request, "eliminar_plan.html", context)

# ------------------------funciones para las views-----------------------------------

def preparar_plan(current_user, request):
    # filter(usuario=current_user)#.all()
    infoUser = InfoUsuario.objects.get(usuario=current_user)
    print(infoUser)
    listaGrupos = Grupo.objects.all()
    listaAlimentos = Alimento.objects.all()
    edad = (
        dt.now().year
        - infoUser.fecha_nacimiento.year
        + (dt.now().month - infoUser.fecha_nacimiento.month) * (1 / 12)
    )

    return render(
        request,
        "generar_plan.html",
        {
            "infoUser": infoUser,
            "edad": edad,
            "listaAlimentos": listaAlimentos,
            "listaGrupos": listaGrupos,
        },
    )


def guardar_plan(req_post, current_user):

    nombre_plan = req_post.get("txtNombrePlan")
    aporte_kcal = int(req_post.get("txtAporteCalorico"))
    print("nombre=" + nombre_plan + " kcal=" + str(aporte_kcal))

    nuevo_plan: Plan = Plan(
        idUsuario=current_user, descripcion=nombre_plan, calorias=aporte_kcal
    )
    nuevo_plan.save()

    llave_comida = ("Desayuno", "Colacion1", "Comida", "Colacion2", "Cena")
    comidas = []
    for comida in llave_comida:
        comidas.append(req_post.getlist(comida))

    i: int = 1
    for comida in comidas:
        tipo_comida: TipoComida = TipoComida.objects.get(idTipoComida=i)
        print(i)
        for id_alimento in comida:
            alimento: Alimento = Alimento.objects.get(idAlimento=id_alimento)
            colacion: Colacion = Colacion(
                idAlimento=alimento, idPlan=nuevo_plan, idTipoComida=tipo_comida
            )
            colacion.save()
        i += 1
    print(str(comidas))
