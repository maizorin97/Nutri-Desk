from django.shortcuts import render, redirect
from . import forms, models

from django.contrib.auth.models import User
from .models import Diagnostico

# Create your views here.
def diagnostico(request):
    if request.method == "POST":
        diagnos_form = forms.FormaDiagnostico(request.POST)
        if diagnos_form.is_valid():
            fd = diagnos_form.save(commit=False)
            fd.idUsuario = User.objects.get(id=request.user.id)
            resultado = genera_diagnostico(fd)
            fd.resultado = resultado
            fd.save()
            return render(request, "diagnostico.html",{"diagnos_form": diagnos_form, "resultado":resultado})
        else:
            return render(request, "diagnostico.html",{"diagnos_form": diagnos_form})
    else:
        diagnos_form = forms.FormaDiagnostico()
        return render(request, "diagnostico.html", {"diagnos_form": diagnos_form})


STD_DATA = {
    "age": {"mean": 53.276852679083916, "std": 6.782098284761919},
    "height": {"mean": 1.6444873569919116, "std": 0.07830064963155765},
    "weight": {"mean": 74.02560810318442, "std": 14.369635645918171},
    "ap_hi": {"mean": 126.48145449245791, "std": 16.535885438250922},
    "ap_lo": {"mean": 81.23238358959411, "std": 9.434938684142596},
    "imc": {"mean": 27.400558527904764, "std": 5.19677882901518},
}


def genera_diagnostico(info:Diagnostico):
    import joblib
    import pandas as pd
    from datetime import datetime as dt

    nombre_archivo = "./diagnosticos/svm_nutridesk_v1.model"
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

    s_list = ["age", "height", "weight", "ap_hi", "ap_lo", "imc"]

    de = STD_DATA

    for column in s_list:
        p_data[column] = (p_data[column]-de[column]['mean'])/de[column]['std']
    
    return modelo_cargado.predict(p_data)[0]