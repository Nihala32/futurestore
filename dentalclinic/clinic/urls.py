from django.urls import path
from clinic import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('register',views.RegistrationView.as_view(),name='register'),
    path('login',views.LoginView.as_view(),name='login'),
    path('home',views.HomeView.as_view(),name='home'),
    path("specialities/all",views.SpecialityListView.as_view(),name='speciality-list'),
    path('specialities/add',views.Add_SpecialityView.as_view(),name='add-speciality'),
    path('doctors/add',views.AddDoctorsView.as_view(),name='add-doctors'),
    path('doctors/all',views.DoctorsListView.as_view(),name='doctors_list'),
    path('signout',views.SignOutView.as_view(),name='signout'),
    path('speciality/change/<int:id>',views.SpecialityEditView.as_view(),name='speciality-edit'),
    path('speciality/remove/<int:id>',views.delete_speciality,name='speciality-remove'),
    path('doctor/edit/<int:id>',views.DoctorEditView.as_view(),name="doctor-edit"),
    path('doctor/remove/<int:id>',views.remove_doctor,name="remove-doctor"),
    path('doctor/details/<int:id>',views.DoctorDetailsView.as_view(),name="detail-doctor")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


