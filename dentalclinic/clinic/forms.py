from django import forms
from clinic.models import Specialities,Doctors
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2",
            "email"
        ]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),

        }

class SpecialityForm(forms.ModelForm):
    class Meta:
        model=Specialities
        fields=['specialty_name']
        widgets={
            "specialty_name" : forms.TextInput(attrs={"class": "form-control"})
        }

class DoctorsForm(forms.ModelForm):

    class Meta:
        model=  Doctors
        fields=["profile_pic",'name','mobile']
    profile_pic=forms.FileField(widget=forms.FileInput(attrs={"class":"form-control"}))

    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # options = (
    #     ("Orthodontics", "Orthodontics"),
    #     ("Endodontist - Root Canal Specialist", "Endodontist - Root Canal Specialist"),
    #     ("Oral and Maxillofacial Surgeon","Oral and Maxillofacial Surgeon"),
    #     ("Pediatric Dentist","Pediatric Dentist"),
    #     ("Periodontist - Gum Specialist","Periodontist - Gum Specialist"),
    #     ("Prosthodontist - Replacement Specialist","Prosthodontist - Replacement Specialist")
    #
    # )
    # specialty=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    mobile=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))


class SpecialityChangeForm(forms.ModelForm):
    class Meta:
        model = Specialities
        fields = "__all__"


class DoctorEditForm(forms.ModelForm):
    class Meta:
        model=Doctors
        exclude=("specialty",)






