from django.contrib.auth.models import User
from django import forms
from postapi.models import Posts
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']
        widgets={

            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"})
        }

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

class AddPostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["title","content","image"]

        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "content": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"})

        }