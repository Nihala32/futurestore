from django.shortcuts import render,redirect
from blogapi.models import *
from django.contrib.auth.models import User
from django.views.generic import CreateView,TemplateView,View,FormView,DetailView,ListView,UpdateView
from mobiles import forms
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

class RagistrationView(CreateView):
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
                    messages.success(request, "")
                    return redirect("dashboard")
                else:
                    return redirect("index")
            else:
                messages.error(request, "invalid credentials")
                return render(request,"login.html",{"form":form})

class IndexView(TemplateView):
    template_name = "index.html"


class MobileListView(ListView):
    template_name = "mobile-list.html"
    form=forms.MobileForm
    context_object_name = "mobiles"


    def get_queryset(self):
        Mobiles.objects.all()


class MobileAddView(CreateView):
    model = Mobiles
    form_class = forms.MobileForm
    template_name = "add-mobile.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

    # def get(self, request, *args, **kwargs):
    #     form = forms.MobileForm()
    #     return render(request, 'add-mobile.html', {'form': form})
    #
    # def post(self, request, *args, **kwargs):
    #     form = forms.MobileForm(request.POST)
    #     if form.is_valid():
    #         form.instance.user = request.user
    #         form.save()
    #         messages.success(request, "book added")
    #         return redirect("index")
    #     else:
    #         messages.error(request, "failed")
    #         return render(request, {"form": form})

