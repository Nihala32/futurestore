from rest_framework import urls
from blog import views
from django.urls import path


urlpatterns=[
    path('register',views.RegistrationView.as_view(),name='register'),
    path('login',views.LoginView.as_view(),name='login'),
    path('home',views.HomeView.as_view(),name='home'),
    path('blog-list',views.BlogListView.as_view(),name='blog-list'),
    path('add-blog',views.AddBlogView.as_view(),name='add-blog'),
    path('signout',views.SignOutView.as_view(),name='signout')


]