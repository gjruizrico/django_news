from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser (AbstractUser):
    age = models.PositiveIntegerField(null=True,blank=True) #null means blank in the DB. Blank is that a value is required.
# Create your models here.
