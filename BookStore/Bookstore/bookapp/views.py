from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,CreateView,TemplateView,ListView,DetailView,UpdateView
from django.contrib.auth import authenticate,login,logout
from bookapp import forms
from bookapp.models import Books
from django.contrib import messages
from bookapp.decorators import signin_required,sign_as_user
from django.utils.decorators import method_decorator


# Create your views here.


class SignUpView(CreateView):
    model = Books
    form_class = forms.RegistrationForm
    template_name = "registration.html"
    success_url =reverse_lazy("signin")
    def form_valid(self, form):
        messages.success(self.request,"Registration successful")
        return super().form_valid(form)

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form = forms.LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if request.user:
                login(request,user)
                if request.user.is_superuser:
                    messages.success(request, "")
                    return redirect("dashboard")
                else:
                    messages.success(request, "login successful")
                    return redirect("userpage")
            else:
                messages.error(request,"invalid Username/password")
                print("invalid credentials")
                return render(request,"login.html",{"form":form})
        return render(request, "login.html")
@method_decorator(signin_required,name="dispatch")
class IndexView(TemplateView):
    template_name = "userpage.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        all_books=Books.objects.all()
        context["books"]=all_books
        return context

@method_decorator(signin_required,name="dispatch")
class UserPageView(TemplateView):
    template_name = "userpage.html"


@method_decorator(signin_required,name="dispatch")
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")





@method_decorator(signin_required,name="dispatch")
class UserBookListView(ListView):
    model = Books
    template_name = "userbook-list.html"
    context_object_name = "books"
    def get_queryset(self):
        return Books.objects.all()





