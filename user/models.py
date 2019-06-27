from django.db import models

# Create your models here.


class User(models.Model):

    email = models.EmailField()
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=64)
    block = models.BooleanField()
    date_created = models.DateTimeField()
