from django.urls import path
from mobiles import views

urlpatterns=[
    path('signup',views.RagistrationView.as_view(),name='signup'),
    path('signin',views.LoginView.as_view(),name='signin'),
    path('index',views.IndexView.as_view(),name='index'),
    path('mobiles/all',views.MobileListView.as_view(),name="mobile-list"),
    path('mobiles/add',views.MobileAddView.as_view(),name="add-mobile")


    ]

