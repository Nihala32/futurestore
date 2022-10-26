from django.urls import path
from patients import views

urlpatterns=[
    path('',views.AdminDashboardView.as_view(),name="home-patient")
]