from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class User(AbstractUser):
    image = models.ImageField(upload_to='profile')


    

 
    class Meta:
        ordering = ('-id',)


