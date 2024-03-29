from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4
import os
# Create your models here.


def file_path(instance, filename):
    ext = filename.rsplit('.')[-1]
    new_name = f"{instance.name}.{ext}"
    return "{0}/{1}".format(instance.user.username, new_name)


class AudioModel(models.Model):
    class Meta:
        ordering = ['date_posted']
        verbose_name = 'Audio'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('audio new name', max_length=100, unique=True, null=False, blank=False)
    hash = models.UUIDField(default=uuid4, unique=True, null=False, editable=False, blank=True)
    audio = models.FileField('audio', upload_to=file_path)
    date_posted = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):

        if os.path.isfile(self.audio.path):
            try:
                os.remove(self.path.path)
                super().delete()
                return True
            except Exception as err:
                return err

        return super().delete()

    def __str__(self):
        return f"{self.audio} - ({self.user})"


class CoverPictureModel(models.Model):
    class Meta:
        ordering = ['date_posted']
        verbose_name = 'Cover Photo'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Cover Picture', max_length=100, unique=True, null=False, blank=False)
    hash = models.UUIDField(default=uuid4, unique=True, null=False, editable=False, blank=True)
    path = models.ImageField('picture',upload_to=file_path)
    date_posted = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):

        if os.path.isfile(self.path.path):
            try:
                os.remove(self.path.path)
                super().delete()
                return True
            except Exception as err:

                return err
        return super().delete()

    def __str__(self):
        return f" {self.name} "

