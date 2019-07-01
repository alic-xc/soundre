from django.db import models
from uuid import uuid4
# Create your models here.
class Users(models.Model):

    username = models.CharField(max_length=150, null=False)
    email = models.EmailField(max_length=250, null=False)
    hash = models.UUIDField(default=uuid4, unique=True, null=False, editable=False )
    password = models.CharField(max_length=80, null=False)
    active = models.BooleanField(default=True, null=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} active ({self.active})"

