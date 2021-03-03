from django import forms
from django.contrib.auth.models import User
from django.db.models import Q

from account.models import AudioModel


class RegistrationForm(forms.ModelForm):
    """ """
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def clean(self):
        """ Check for email and username """
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        try:

            user = User.objects.get(Q(email=email)|Q(username=username))
            if user:
                raise forms.ValidationError('Email/Username already exist. Please choose another and try again')

        except User.DoesNotExist:
            pass

        return self.cleaned_data


class LoginForm(forms.Form):
    """ """
    username = forms.CharField(widget=forms.TextInput({'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Enter password'}))


class UploadAudioForm(forms.ModelForm):
    class Meta:
        model = AudioModel
        fields = ['name', 'audio']
        widgets = {
            'audio': forms.FileInput({'accept': 'audio/mpeg', 'class': 'form-control'}),
            'name': forms.TextInput({'class': 'form-control'})
        }

    def clean_audio(self):
        """ Validate audio size and type """
        audio = self.cleaned_data['audio']
        FILE_EXT = ['mp3']
        errors = []
        # Check for file size
        if round(audio.size / 1024) < 0 or round(audio.size / 1024) > 10000:
            errors.append({'audio': 'Check file size. Unsupported size'})

        # Check for file format
        if str(audio.name).split('.')[-1] not in FILE_EXT:
            errors.append({'audio': 'Check audio type. supported format is mp3'})

        if len(errors) > 0:
            raise forms.ValidationError(errors)

        return audio

