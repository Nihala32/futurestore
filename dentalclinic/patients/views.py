from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import TemplateView,ListView,DetailView
from django.core.mail import send_mail

class AdminDashboardView(TemplateView):
    template_name = "patients.html"