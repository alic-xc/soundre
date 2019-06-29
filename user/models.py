from django.db import models
from uuid import uuid4
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField('Email Address')
    password = models.CharField('Password', max_length=64)
    hash = models.UUIDField('User Key', default=uuid4(), unique=True, editable=False)
    block = models.BooleanField('activate', default=False)
    date_created = models.DateTimeField('date created', auto_now_add=True)

    def __str__(self):

        return f'{self.username} - ({self.date_created})'


