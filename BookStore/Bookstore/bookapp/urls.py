from django.urls import path,include
from bookapp import views

urlpatterns = [
    path('register', views.SignUpView.as_view(), name="register"),
    path("", views.LoginView.as_view(), name="signin"),
    path("home", views.IndexView.as_view(), name="userpage"),
    # path("userpage", views.UserPageView.as_view(), name="userpage"),
    path("signout", views.SignOutView.as_view(), name="signout"),
    path("userbook/all", views.UserBookListView.as_view(), name="userbooklist"),



]
