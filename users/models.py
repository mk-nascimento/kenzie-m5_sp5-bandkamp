from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    full_name = models.CharField(max_length=50)
    artistic_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
