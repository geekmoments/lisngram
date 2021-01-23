"""posts models"""

#django
from django.db import models

# Create your models here.

class User(models.Model):

    is_admin = models.BooleanField(default=False)

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField(blank=True,null=True)

    bio = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modifies = models.DateTimeField(auto_now=True)

