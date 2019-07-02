from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4
import os
# Create your models here.


def file_path(instance, filename):
    ext = filename.rsplit('.')[-1]
    new_name = f"{instance.name}.{ext}"
    return "audio/{0}/{1}".format(instance.user.username, new_name)


class AudioModel(models.Model):
    class Meta:
        ordering = ['date_posted']
        verbose_name = 'Audio'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('audio new name', max_length=100, unique=True, null=False, blank=False)
    hash = models.UUIDField(default=uuid4(), unique=True, null=False, editable=False, blank=True)
    path = models.FileField('audio', upload_to= file_path)
    date_posted = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.path} - ({self.hash})"


