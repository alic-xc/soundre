from django import forms
from django.core.files import File
from django.contrib.auth.models import User
from django.forms import BaseInlineFormSet
from .models import CoverPictureModel


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 'password', 'email'
        ]


class EditUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput({'placeholder': 'Enter username'}))
    email = forms.EmailField(widget=forms.EmailInput({'placeholder': 'Enter email'}))


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput({'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Enter password'}))


# class ShortAudioForm(forms.Form):
    # CHOICES = [('Beginning','beginning'),('End','end')]
    # audio = forms.FileField(widget=forms.FileInput({
    #                         'accept':'.mp3',
    #                     }))
    # seconds = forms.IntegerField(label='delayed seconds',
    #                              widget=forms.NumberInput({'min': 0, 'max': 10, 'size':2,'placeholder':'Enter Delayed Seconds'}))
    # position = forms.ChoiceField(label='Sound Position', choices=CHOICES)
    # volume = forms.IntegerField(label='volume',
    #                             widget=forms.NumberInput({'min': -10, 'max': -1, 'size':2,'placeholder':'Enter Custom Sound Volume'}))
    #
    # def clean_audio(self, *args, **kwargs):
    #     audio = File(self.cleaned_data['audio'])
    #     filesize = round(audio.size/ 1024)
    #     if filesize > 1024:
    #         forms.ValidationError('Audio size error. required less than 1mb')
    #     return audio
    #
    # def clean_seconds(self, *args, **kwargs):
    #     seconds = self.cleaned_data['seconds']
    #     if seconds < 0 or seconds  > 10:
    #         forms.ValidationError('Seconds invalid. check delayed seconds')
    #     return seconds * 1000
    #
    # def clean_volume(self, *args, **kwargs):
    #     volume = self.cleaned_data['volume']
    #     if volume  > -1 or volume  < -10:
    #         forms.ValidationError
    #
    #     return volume


class AudioRangeForm(forms.Form):
    minute = forms.IntegerField(widget=forms.NumberInput({'min':0, 'placeholder':'Enter Position Minute'}))
    seconds = forms.IntegerField(widget=forms.NumberInput({'min':0,'max':59, 'placeholder':'Enter Position Seconds'}))
    length = forms.IntegerField(widget=forms.NumberInput({'min':0, 'max':59, 'placeholder':'Enter Length To Remove'}))


class AudioTagsForm(forms.Form):
    title = forms.CharField(required=False, widget=forms.TextInput({'placeholder': "Enter Song Title"}))
    album = forms.CharField(required=False, widget=forms.TextInput({'placeholder': "Enter Song's Album "}))
    composer = forms.CharField(required=False, widget=forms.TextInput({'placeholder': "Enter Song's Composer"}))
    copyright = forms.ChoiceField(required=False, choices=[('-- Select Copyright Status --', ''), ('yes', 'yes'), ('no', 'no')])
    artist = forms.CharField(required=False, widget=forms.TextInput({'placeholder': "Enter Artist Name"}))
    albumartist = forms.CharField(label='album artist', required=False, widget=forms.TextInput({'placeholder': "Enter Album Artist"}))
    author = forms.CharField(required=False, widget=forms.TextInput({'placeholder': "Enter Song Author"}))
    language = forms.CharField(required=False, widget=forms.TextInput({'placeholder': "Enter Song Language"}))
    genre = forms.CharField(required=False, widget=forms.TextInput({'placeholder': "Enter Song Genre"}))
    date = forms.CharField(required=False, widget=forms.TextInput({'placeholder': "Enter Song Date"}))
    cover = forms.ModelChoiceField(required=False, queryset=CoverPictureModel.objects.all(),label='cover picture', empty_label='--Select Cover Picture--')


class BaseCoverPictureSet(BaseInlineFormSet):

    def clean(self):
        super().clean()
        path = []
        for form in self.forms:

            picture = File(form.cleaned_data['path'])
            filezise = round(picture / 1024)
            if filezise < 0 or filezise > 100:
                raise forms.ValidationError('Picture Size no valid. resize picture')
            path.append(picture)


class UploadForm(forms.Form):
    audio = forms.FileField(widget=forms.FileInput({'accept':'.mp3'}))

