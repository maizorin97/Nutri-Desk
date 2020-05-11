from django import forms
from .models import InfoUsuario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class FormaInicioSesion(AuthenticationForm):
    username = forms.EmailField(label="Correo Electrónico", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escriba su correo electrónico'}
    ), min_length=5, max_length=100)

    password = forms.CharField(label="Contraseña", required=True, widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Escriba su contraseña'}
    ), min_length=5, max_length=100)

    class Meta:
        model = User
        fields = ('username', 'password')

class FormaRegistroUsuario(UserCreationForm):
    username = forms.EmailField(label="Correo Electrónico", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Correo Electrónico'}
    ), min_length=5, max_length=100)

    password1 = forms.CharField(label="Nueva contraseña", required=True, widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Nueva contraseña'}
    ), min_length=5, max_length=100)

    password2 = forms.CharField(label="Confirmacón de contraseña", required=True, widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Confirmacón de contraseña'}
    ), min_length=5, max_length=100)

    first_name = forms.CharField(label="Nombre(s)", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Nombre(s)'}
    ), min_length=2, max_length=100)

    last_name = forms.CharField(label="Apellido(s)", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Apellido(s)'}
    ), min_length=2, max_length=200)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name')

class FormaDatosFisiologicos(forms.ModelForm):
    fecha_nacimiento = forms.DateField(label="Fecha de nacimiento" ,required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Fecha de nacimiento','type':'date'}))
    altura = forms.FloatField(label="Altura en centimetros", required=True, widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder':'Altura en centimetros'}))
    peso = forms.FloatField(label="Peso en kilogramos", required=True, widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder':'Peso en kilogramos'}))
    sexo = forms.CharField(label="Sexo", required=True, widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'Elige tu sexo'}, choices=(('H','Hombre'),('M','Mujer'))))
    class Meta:
        model = InfoUsuario
        fields = ('fecha_nacimiento', 'altura', 'peso', 'sexo')