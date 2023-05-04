from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin   
# from challenges.models import Challenges

class User_info(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100,unique=True)
    email = models.EmailField(primary_key=True)
    task1 = models.IntegerField(default=0)
    task2 = models.IntegerField(default=0)
    task3 = models.IntegerField(default=0)
    task4 = models.IntegerField(default=0)
    task5 = models.IntegerField(default=0)
    task6 = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)




# class User_info(AbstractBaseUser, PermissionsMixin):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=100,unique=True)
#     email = models.EmailField(unique=True)

#     USERNAME_FIELD = 'phone'
#     REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

#     def __str__(self):
#         return self.phone

#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"

#     def get_short_name(self):
#         return self.first_name