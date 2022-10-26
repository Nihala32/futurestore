from django.urls import path
from social import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('login',views.LoginView.as_view(),name="signin"),
    path('register',views.RegistrationView.as_view(),name="signup"),
    path('posts/add',views.AddPostView.as_view(),name="add-post"),
    path('home',views.HomeView.as_view(),name="index"),
    path("signout", views.SignOutView.as_view(), name="signout"),
    path('posts/all',views.PostListView.as_view(),name='list-post'),
     path("products/<int:id>/", views.UserDetailView.as_view(), name="user-detail"),

            ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

