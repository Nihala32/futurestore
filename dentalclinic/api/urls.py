from api.views import SpecialityView,DoctorsView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

router=DefaultRouter()
router.register("specialities",SpecialityView,basename="specialities"),
router.register('doctors',DoctorsView,basename="doctors")



urlpatterns=[
                path('accounts/token', obtain_auth_token),

            ]+router.urls