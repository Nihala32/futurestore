from django.shortcuts import render,redirect
from social import forms
from django.views.generic import View,CreateView,UpdateView,ListView,DetailView,DeleteView,TemplateView
from django.contrib.auth.models import User
from postapi.models import Posts,Userprofile
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout

class RegistrationView(CreateView):
    model = User
    form_class = forms.RegistrationForm
    template_name = "register.html"
    success_url = reverse_lazy("signin")

    def form_valid(self, form):
        # messages.success(self.request, "your account has been created")
        return super().form_valid(form)

    # def get(self,request,*args,**kwargs):
    #     form=forms.RegistrationForm()
    #     return render(request,"register.html",{"form":form})
    # def post(self,request,*args,**kwargs):
    #     form=forms.RegistrationForm(request.POST)
    #     if form.is_valid():
    #         User.objects.create_user(**form.cleaned_data)
    #     return render(request,"register.html",{"form":form})

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=forms.LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            usrnm=form.cleaned_data.get("username")
            psw=form.cleaned_data.get("password")
            user=authenticate(username=usrnm,password=psw)
            if user:
                login(request,user)
                return redirect("index")

        return render(request,'login.html')

class HomeView(TemplateView):
    template_name = "home.html"

class AddPostView(CreateView):
    model = Posts
    template_name = "add-post.html"
    form_class = forms.AddPostForm
    success_url = reverse_lazy("add-post")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")


class PostListView(ListView):
    model = Posts
    template_name = "list-post.html"
    context_object_name = "posts"
    def get_queryset(self):
        return Posts.objects.all()

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        all_products=Posts.objects.all()
        context["products"]=all_products
        return context

class UserDetailView(DetailView):
    template_name = "home.html"
    model = Userprofile
    context_object_name = "profile"
    pk_url_kwarg = "id"
