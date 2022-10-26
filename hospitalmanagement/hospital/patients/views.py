from django.shortcuts import render,redirect
from patients.models import *
from django.contrib.auth.models import User
from django.views.generic import CreateView,TemplateView,View,FormView,DetailView,ListView,UpdateView
from patients import forms
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.

class RageistrationView(CreateView):
    form_class = forms.UserRegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("login")

class LoginView(FormView):
    template_name = "login.html"
    form_class = forms.LoginForm

    def post(self,request,*args,**kwargs):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                if request.user.is_superuser:
                    messages.success(request, "login successfull")
                    return redirect("dashboard")
                else:
                    messages.success(request, "login successfull")
                    return redirect("home")
            else:
                messages.error(request, "invalid credentials")
                return render(request,"login.html",{"form":form})