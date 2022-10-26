from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from blogapi.models import Mobiles


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model=User
        fields=[
            "username",
            "password1",
            "password2",
            "email"
        ]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"})

        }


class MobileForm(forms.ModelForm):
    class Meta:
        model=Mobiles
        fields=['name',"price","band","display","processor"]
        widgets={
            "name" : forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "band": forms.TextInput(attrs={"class": "form-control"}),
            "display": forms.TextInput(attrs={"class": "form-control"}),
            "processor": forms.TextInput(attrs={"class": "form-control"}),

        }