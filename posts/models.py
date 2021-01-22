"""posts models"""

#django
from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField()
    password = models.CharField()

    first_name = models.CharField()
    last_name = models.CharField()
    birthdate = models.DateField()

    bio = models.TextField()

    created = models.DateTimeField()
    modifies = models.DateTimeField()
    
