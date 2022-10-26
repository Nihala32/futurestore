from rest_framework import serializers
from clinic.models import Specialities,Doctors


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Specialities
        fields="__all__"

class DoctorSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    specialty=serializers.CharField(read_only=True)
    class Meta:
        model=Doctors
        fields=[
            "id",
            "profile_pic",
            "name",
            "specialty",
            "mobile",
            "status"
        ]



