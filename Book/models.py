from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    email = models.EmailField('email', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# Create your models here.
