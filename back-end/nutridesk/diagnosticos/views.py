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
            resultado = 0
            fd.resultado = resultado
            print(fd.idUsuario)
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
