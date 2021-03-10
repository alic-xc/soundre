from django import forms
from django.core.files import File


class MergeForm(forms.Form):
    """ """
    CHOICES = (('Beginning', 'beginning'), ('End', 'end'))
    audio = forms.FileField(widget=forms.FileInput({'accept': '.mp3', 'class': 'form-control'}))
    seconds = forms.IntegerField(widget=forms.NumberInput({'min': 0, 'max': 10, 'size': 2,
                                                           'class': 'form-control',
                                                           'placeholder': 'Enter Delayed Seconds'}))
    position = forms.ChoiceField(choices=CHOICES, widget=forms.Select({'class': 'form-control'}))

    def clean_audio(self):
        audio = File(self.cleaned_data['audio']) # Convert to file object for other usage
        filesize = round(audio.size / 1024)
        if filesize > 1024:
            forms.ValidationError('Audio size error. required less than 1mb')
        return audio

    def clean_seconds(self):
        seconds = self.cleaned_data['seconds']
        if seconds < 0 or seconds > 10:
            forms.ValidationError('Seconds invalid. check delayed seconds')
        return seconds * 1000
