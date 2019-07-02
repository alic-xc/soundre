from django import forms
from django.contrib.auth.models import User
from .models import AudioModel


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 'password', 'email'
        ]


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput({'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Enter password'}))

class ShortFileForm(forms.Form):
    audio = forms.FileField(widget=forms.FileInput({
                            'accept':'.mp3',
                        }))

# class FileUploadForm(forms.ModelForm):
#
#     class Meta:
#         model = AudioModel
#         fields = ['name', 'path', 'user']
#         widgets = {
#             'path': forms.FileInput({'accept':'.mp3'}),
#             'user': forms.HiddenInput()
#         }
