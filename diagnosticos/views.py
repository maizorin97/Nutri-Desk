from django.shortcuts import render, redirect
from . import forms, models

from django.contrib.auth.models import User
from .models import DiagnosticoCardio, DiagnosticoObesidad

import joblib
import pandas as pd
from datetime import datetime as dt

# Create your views here.
def diagnostico(request):
    
    if request.method == "POST" and "btnDiagnosticoCardio" in request.POST:
        diagnos_form = forms.FormaDiagnosticoCardio(request.POST)
        if diagnos_form.is_valid():
            fd = diagnos_form.save(commit=False)
            fd.idUsuario = User.objects.get(id=request.user.id)
            resultado = genera_diagnostico_cardio(fd)
            fd.resultado = resultado
            fd.save()
            return render(request, "diagnostico.html",{"diagnos_form": diagnos_form, "resultado":resultado})
        else:
            return render(request, "diagnostico.html",{"diagnos_form": diagnos_form})
    
    elif request.method == "POST" and "btnDiagnosticoObesidad" in request.POST:
        obes_form = forms.FormaDiagnosticoObesidad(request.POST)
        if obes_form.is_valid():
            fd = obes_form.save(commit=False)
            fd.idUsuario = User.objects.get(id=request.user.id)
            resultado = genera_diagnostico_obesidad(fd)
            fd.nobeyesdad = resultado
            fd.save()
            return render(request, "diagnostico.html",{"obes_form": obes_form, "resultado":resultado})
        else:
            print("La forma no es valida")
            return render(request, "diagnostico.html",{"obes_form": obes_form})
    else:
        diagnos_form = forms.FormaDiagnosticoCardio()
        obes_form= forms.FormaDiagnosticoObesidad()
        result_cardio= DiagnosticoCardio.objects.all()
        result_obes= DiagnosticoObesidad.objects.all()
        print(result_cardio)
        return render(request, "diagnostico.html", {"diagnos_form": diagnos_form, "obes_form":obes_form, "result_cardio":result_cardio, "result_obes":result_obes})


def genera_diagnostico_cardio(info:DiagnosticoCardio):
    nombre_archivo = "./diagnosticos/cardio_nutridesk_v1.model"
    modelo_cargado = joblib.load(nombre_archivo)

    age = (
        dt.now().year
        - info.fecha_nacimiento.year
        + (dt.now().month - info.fecha_nacimiento.month) * (1 / 12)
    )

    sex = 0
    if info.sexo == 'H':
        sex = 1
    
    heigth = info.altura/100

    imc = info.peso / heigth**2

    prueba =[[age,sex,heigth,info.peso,info.pres_hi,info.pres_lo,info.colesterol,
    info.glucosa,info.fumador,info.alcoholico,info.deporte,imc]]

    p_data = pd.DataFrame(data=prueba, columns = ['age','gender','height','weight','ap_hi',
        'ap_lo','cholesterol','gluc','smoke','alco','active','imc'])
    
    return modelo_cargado.predict(p_data)[0]


def genera_diagnostico_obesidad(info:DiagnosticoObesidad):
    nombre_archivo = "./diagnosticos/obesidad_nutridesk_v1.model"
    modelo_cargado = joblib.load(nombre_archivo)

    edad = (
        dt.now().year
        - info.edad.year
        + (dt.now().month - info.edad.month) * (1 / 12)
    )

    prueba =[[info.genero,edad,info.altura,info.peso,info.historial_obesidad,info.favc,
            info.fcvc,info.npc,info.caec,info.smoke,info.ch2o,info.scc,info.faf,info.tue,info.calc,info.mtrans]]

    p_data = pd.DataFrame(data=prueba, columns = ['Gender','Age','Height','Weight','family_history_with_overweight',
        'FAVC','FCVC','NPC','CAEC','SMOKE','CH2O','SCC','FAF','TUE','CALC','MTRANS'])
    
    return modelo_cargado.predict(p_data)[0]