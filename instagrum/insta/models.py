from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class MyUser(AbstractUser):
    login = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.TextField()
    bio = models.TextField()


class Photo(models.Model):
    path = models.CharField(max_length=250)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)



