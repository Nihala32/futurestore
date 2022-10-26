from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,UpdateView,ListView,FormView,TemplateView
from django.contrib.auth.models import User
from blog import forms
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from blogapi.models import Blogs
# Create your views here.

class RegistrationView(CreateView):
    template_name = "registration.html"
    form=forms.UserRegistrationForm
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
                    return redirect("home")
            else:
                messages.error(request, "invalid credentials")
                return render(request,"login.html",{"form":form})

class HomeView(TemplateView):
    template_name = "home.html"


class BlogListView(ListView):
    template_name = "blog-list.html"
    model = Blogs
    context_object_name = "blogs"

    def get_queryset(self):
        return Blogs.objects.all()


class AddBlogView(CreateView):
    template_name = 'add-blog.html'
    form_class = forms.BlogForm
    success_url = reverse_lazy("home")

class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")






