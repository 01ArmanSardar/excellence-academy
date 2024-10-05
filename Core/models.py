from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     is_active=models.BooleanField(default=False)

class UserEducation(models.Model):
    user=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    schoolName=models.CharField(max_length=50)
    classs=models.CharField(max_length=50)
    RollNo=models.IntegerField()