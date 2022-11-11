from django import forms
from .models import  EducationLevel,Flights, Birth
from django.forms import TextInput, EmailInput


        
class BirthForm(forms.ModelForm):
    class Meta:
        model = Birth
        fields = '__all__'
        widgets = {
            'year': TextInput(attrs={
                    'class': "form-control my-2",
                    'placeholder': 'Year'
                }),
            'cantidad': TextInput(attrs={
                'class': "form-control my-2",
                'placeholder': 'Amount'
                }),
        }
        
class EducationLevelForm(forms.ModelForm):
    class Meta:
        model = EducationLevel
        fields = '__all__'
        widgets = {
            'year': TextInput(attrs={
                    'class': "form-control my-2",
                    'placeholder': 'Year'
                }),
            'cantidad': TextInput(attrs={
                'class': "form-control my-2",
                'placeholder': 'Amount'
                }),
        }

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flights
        fields = '__all__'
        widgets = {
            'year': TextInput(attrs={
                    'class': "form-control my-2",
                    'placeholder': 'Year'
                }),
            'cantidad': TextInput(attrs={
                'class': "form-control my-2",
                'placeholder': 'Amount'
                }),
        }

