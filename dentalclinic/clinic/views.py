from django.shortcuts import render,redirect
from clinic import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView,View,FormView,DetailView,ListView,UpdateView
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from clinic.models import Specialities,Doctors

# Create your views here.

class RegistrationView(CreateView):
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
                    return redirect("home")
                else:
                    messages.success(request, "login successfull")
                    return redirect("home-patient")
            else:
                messages.error(request, "invalid credentials")
                return render(request,"login.html",{"form":form})

class HomeView(TemplateView):
    template_name = "home.html"


class SpecialityListView(ListView):
    template_name = "speciality_list.html"
    context_object_name = "specialities"
    model= Specialities


    def get(self, request, *args, **kwargs):
        all = Specialities.objects.all()
        return render(request, 'speciality_list.html', {"specialities": all})

class Add_SpecialityView(CreateView):
    model = Specialities
    template_name = "add_speciality.html"
    form_class = forms.SpecialityForm
    success_url = reverse_lazy('speciality-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddDoctorsView(CreateView):
    model=Doctors
    template_name = "add-doctors.html"
    form_class = forms.DoctorsForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class DoctorsListView(ListView):
    template_name = "doctors_list.html"
    context_object_name = "doctors"
    model= Doctors


    def get(self, request, *args, **kwargs):
        doctors = Doctors.objects.all()
        return render(request, 'doctors_list.html', {"doctors": doctors})


class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")


class SpecialityEditView(UpdateView):
    model=Specialities
    form_class = forms.SpecialityChangeForm
    template_name = "Speciality-edit.html"
    success_url = reverse_lazy("speciality-list")
    pk_url_kwarg = "id"

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)


def delete_speciality(request,*args,**kwargs):
    id=kwargs.get("id")
    Specialities.objects.get(id=id).delete()
    return redirect('speciality-list')


class DoctorEditView(UpdateView):
    model=Doctors
    form_class = forms.DoctorEditForm
    template_name = "doctor-edit.html"
    success_url = reverse_lazy("doctors_list")
    pk_url_kwarg = "id"

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)


def remove_doctor(request,*args,**kwargs):
    id=kwargs.get("id")
    Doctors.objects.get(id=id).delete()
    return redirect("doctors_list")


class DoctorDetailsView(DetailView):
    model=Doctors
    template_name = "doctor-detail.html"
    context_object_name = "doctor"
    pk_url_kwarg = "id"
