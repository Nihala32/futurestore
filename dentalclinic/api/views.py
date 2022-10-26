from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import permission_classes

from api.serializers import SpecialitySerializer,DoctorSerializer
from django.contrib.auth.models import User
from clinic.models import Specialities,Doctors
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.

class SpecialityView(viewsets.ModelViewSet):
    serializer_class = SpecialitySerializer
    queryset = Specialities.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=["get"],detail=True)
    def get_doctors(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        speciality=Specialities.objects.get(id=id)
        doctor=speciality.doctors_set.all()
        serializer=DoctorSerializer(doctor,many=True)
        return Response(data=serializer.data)

    @action(methods=["post"],detail=True)
    def add_doctor(self,request,*args,**kwargs):
        user=request.user
        id=kwargs.get("pk")
        speciality=Specialities.objects.get(id=id)
        serializer=DoctorSerializer(data=request.data,context={"speciality":speciality,'user':user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)






class DoctorsView(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctors.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]



