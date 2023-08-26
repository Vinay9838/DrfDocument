from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    gender = models.CharField(choices=(('M','Male'),('F','Female')),max_length=20, null=True, blank=True)
    blood_group = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    photo = models.FileField(upload_to='profile', null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username