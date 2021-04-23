from django import forms
from .models import Diagnostico

class FormaDiagnostico(forms.ModelForm):
    fecha_nacimiento = forms.DateField(label="Fecha de nacimiento", required=True, widget=forms.DateInput(
        attrs={'class':'form-control', 'placeholder':'Fecha de nacimiento','type':'date'}))
    altura = forms.FloatField(label="Altura en centimetros", required=True, widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder':'Altura'}))
    peso = forms.FloatField(label="Peso en kilogramos", required=True, widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder':'Peso'}))
    sexo = forms.CharField(label="Sexo", required=True, widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'Elige tu sexo'}, choices=(('H','Hombre'),('M','Mujer'))))
    pres_hi = forms.IntegerField(label="Presion arterial sistólica", required=True, widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder':'Presion arterial sistólica'}))
    pres_lo = forms.IntegerField(label="Presion arterial diastólica", required=True, widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder':'Presion arterial diastólica'}))
    fumador = forms.CharField(label="¿Es fumador?", required=True, widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'¿Es fumador?'}, choices=((0,'No'),(1,'Si'))))
    alcoholico = forms.CharField(label="¿Bebe alcohol?", required=True, widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'¿Bebe alcohol?'}, choices=((0,'No'),(1,'Si'))))
    deporte = forms.CharField(label="¿Realiza deporte?", required=True, widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'¿Realiza deporte?'}, choices=((0,'No'),(1,'Si'))))
    glucosa = forms.CharField(label="Nivel de glucosa", required=True, widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'Glucosa'}, choices=((0,'Normal'),(1,'Arriba de lo normal'),(2,'Muy arriba de lo normal'))))
    colesterol = forms.CharField(label="Nivel de colesterol", required=True, widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'Colesterol'}, choices=((0,'Normal'),(1,'Arriba de lo normal'),(2,'Muy arriba de lo normal'))))
    class Meta:
        model = Diagnostico
        fields = ('colesterol', 'glucosa', 'fecha_nacimiento', 'altura', 'peso', 'sexo', 'pres_hi', 'pres_lo','fumador', 'alcoholico', 'deporte')