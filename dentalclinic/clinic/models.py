from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.template.defaultfilters import slugify
import os


# Create your models here.
class Specialities(models.Model):
    specialty_name = models.CharField(max_length=120, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        self.specialty_name


class Doctors(models.Model):
    profile_pic = models.ImageField(upload_to="Images", null=True, default=None)
    name = models.CharField(max_length=120,null=True)
    specialty = models.ForeignKey(Specialities, on_delete=models.CASCADE, null=True)
    mobile = models.PositiveIntegerField(null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# class Patients(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     address=models.CharField(max_length=120)
#     mobile=models.PositiveIntegerField(validators=[MinValueValidator(10),MaxValueValidator(10)])

class Appointment(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    email = models.EmailField(max_length=50)
    mobile = models.PositiveIntegerField()
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    date = models.DateTimeField()
