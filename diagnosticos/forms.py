from django import forms
from .models import DiagnosticoCardio, DiagnosticoObesidad

class FormaDiagnosticoCardio(forms.ModelForm):
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
        model = DiagnosticoCardio
        fields = ('colesterol', 'glucosa', 'fecha_nacimiento', 'altura', 'peso', 'sexo', 'pres_hi', 'pres_lo','fumador', 'alcoholico', 'deporte')

class FormaDiagnosticoObesidad(forms.ModelForm):
    fecha_nacimiento = forms.DateField(label="Fecha de nacimiento", required=True, widget=forms.DateInput(
        attrs={'class':'form-control', 'placeholder':'Fecha de nacimiento','type':'date'}))
    altura = forms.FloatField(label="Altura en centimetros", required=True, widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder':'Altura'}))
    peso = forms.FloatField(label="Peso en kilogramos", required=True, widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder':'Peso'}))
    genero = forms.CharField(label="Genero", required=True, widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'Elige tu sexo'}, choices=((1,'Hombre'),(0,'Mujer'))))
    historial_obesidad = forms.CharField(label="¿Existen antecedentes de obesidad en su familia?", required=True, widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'Antecedentes de Obesidad'}, choices=((0,'No'),(1,'Si'))))
    favc = forms.CharField(label="¿Consume frecuentemente alimentos altos en calorías?", required=True, widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'Consumo de alimentos altos en calorías'}, choices=((0,'No'),(1,'Si'))))
    fcvc = forms.CharField(label="¿Cada cuándo consume vegetales?", required=True, widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'Consumo de vegetales'}, choices=((0,'Nunca'),(1,'Algunas Veces'), (2,'Siempre'))))
    npc = forms.CharField(label="Comidas principales al día", required=True, widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'Comidas principales'}, choices=((0,'Entre 1 y 2'),(1,'Tres'), (2,'Más de tres'))))
    caec = forms.CharField(label="¿Come alimentos entre comidas?", required=True, widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'Alimentos entre comidas'}, choices=((0,'Siempre'),(1,'Frecuntemente'), (2,'Algunas veces'), (3,'No'))))
    smoke = forms.CharField(label="¿Es fumador?", required=True, widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'¿Es fumador?'}, choices=((0,'No'),(1,'Si'))))
    ch2o = forms.CharField(label="Consumo de agua al día", required=True, widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'Cantidad de agua'}, choices=((0,'Menos de un litro'),(1,'Entre 1 y 2 litros'), (2,'Más de 2 litros')))) 
    scc = forms.CharField(label="¿Monitorea su consumo de calorías?", required=True, widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'Respuesta'}, choices=((0,'No'),(1,'Si'))))
    faf = forms.CharField(label="Frecuencia de actividad física", required=True, widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'Frecuencia'}, choices=((0,'No practica'),(1,'1 a 2 días por semana'), (2,'2 a 4 días por semana'), (3,'3 a 5 días por semana'))))
    tue= forms.CharField(label="Tiempo de uso de dispositivos móviles", required=True, widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'Tiempo de uso'}, choices=((0,'0 a 2 horas al día'),(1,'3 a 5 horas al día'), (2,'Más de 5 horas al día'))))
    calc = forms.CharField(label="Frecuencia de consumo de alcohol", required=True, widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'Frecuencia'}, choices=((0,'Siempre'),(1,'Frecuentemente'), (2,'Algunas veces'), (3,'No'))))
    mtrans = forms.CharField(label="Medio de transporte principal", required=True, widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'Medio de transporte'}, choices=((0,'Automóvil'),(1,'Motocicleta'), (2,'Bicicleta'), (3,'Transporte Público'), (4,'Caminar'))))

    class Meta:
        model = DiagnosticoObesidad
        fields = ('fecha_nacimiento', 'altura', 'peso', 'genero', 'historial_obesidad', 
        'favc', 'fcvc', 'npc', 'caec', 'smoke', 'ch2o' ,'scc', 'faf', 'tue', 'calc', 'mtrans')
