from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic import CreateView, ListView, TemplateView

from .models import Plan, TipoComida, Colacion
from core.models import InfoUsuario
from smae.models import Alimento, Grupo
from django.contrib.auth.models import User
import json
from datetime import datetime as dt
from django.core import serializers

class lista_planes(ListView):
    template_name = "generar_plan.html"
    model = Plan
    context_object_name = "lista_planes"

    def get_context_data(self, **kwargs):
        context = super(lista_planes, self).get_context_data(**kwargs)
        infoUser = InfoUsuario.objects.get(usuario=self.request.user)
        edad = (
            dt.now().year
            - infoUser.fecha_nacimiento.year
            + (dt.now().month - infoUser.fecha_nacimiento.month) * (1 / 12)
        )
        context.update({
            "infoUser": infoUser,
            "edad": edad,
            #"listaAlimentos": listaAlimentos,
            #"listaGrupos": listaGrupos,
        })
        return context
    
    def guardar_plan(self,req_post, current_user):
        nombre_plan = req_post.get("txtNombrePlan")
        print(req_post.get("txtAporteCalorico"))
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

    def post(self, request, *args, **kwargs):
        usuario: User = InfoUsuario.objects.get(usuario=request.user).usuario
        self.guardar_plan(request.POST, usuario)
        
        return redirect("planes") 
        
    def delete(self,request, *args, **kwargs):
        plan_id=request.body.decode("UTF-8")
        obj_plan = get_object_or_404(Plan, idPlan=plan_id)
        obj_plan.delete()
        return HttpResponse(json.dumps({}))
    
    def get(self, *args, **kwargs):
        plan_id=self.request.GET.get("plan_id")
        if (plan_id != None):
            plan = Plan.objects.get(idPlan=plan_id)
            colaciones = Colacion.objects.filter(idPlan=plan)
            colaciones_arr=[]
            for colacion in colaciones:
                colaciones_arr.append({
                    "tipoComida":colacion.idTipoComida.nombre,
                    "nombre":colacion.idAlimento.nombre,
                    "racion":colacion.idAlimento.racion,
                    "grupo":colacion.idAlimento.idGrupo.nombre
                })
            return HttpResponse(json.dumps(colaciones_arr))
        else:
            resp = super().get(*args, **kwargs)
            return resp
    
def generar_planes(request):
    if request.method == "POST":
        usuario: User = InfoUsuario.objects.get(usuario=request.user).usuario
        guardar_plan(request.POST, usuario)
        return redirect("planes")
    else:
        return preparar_plan(request.user, request)

def get_datos(request):
    ##medir tiempos
    listaGrupos = Grupo.objects.all()
    listaAlimentos = Alimento.objects.all()
    grupos=[]
    alimentos=[]
    for grupo in listaGrupos:
        grupos.append({"nombre":grupo.nombre})
    for alimento in listaAlimentos:
        alimentos.append({
            "idGrupo":alimento.idGrupo.nombre,
            "nombre":alimento.nombre,
            "idAlimento":alimento.idAlimento,
            "energia":alimento.idGrupo.energia,
            "proteina":alimento.idGrupo.proteina            
        })
     
    return HttpResponse(json.dumps({"listaGrupos":grupos,"listaAlimentos":alimentos}))






