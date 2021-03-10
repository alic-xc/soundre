from django import forms
from django.core.files import File


class TagForm(forms.Form):
    """ """
    title = forms.CharField(required=False, widget=forms.TextInput({'placeholder': "Enter Song Title",
                                                                    "class": "form-control"}))
    album = forms.CharField(required=False, widget=forms.TextInput({'placeholder': "Enter Song's Album ",
                                                                    "class": "form-control"}))
    composer = forms.CharField(required=False, widget=forms.TextInput({'placeholder': "Enter Song's Composer",
                                                                       "class": "form-control"}))
    copyright = forms.ChoiceField(required=False,
                                  choices=[(' ', '-- Select Copyright Status --'), ('yes', 'yes'), ('no', 'no')],
                                  widget=forms.Select({'class': 'form-control'}))
    artist = forms.CharField(required=False, widget=forms.TextInput({'placeholder': "Enter Artist Name",
                                                                     "class": "form-control"}))
    albumartist = forms.CharField(label='album artist', required=False,
                                  widget=forms.TextInput({'placeholder': "Enter Album Artist",
                                                          "class": "form-control"}))
    author = forms.CharField(required=False, widget=forms.TextInput({'placeholder': "Enter Song Author",
                                                                     "class": "form-control"}))
    language = forms.CharField(required=False, widget=forms.TextInput({'placeholder': "Enter Song Language",
                                                                       "class": "form-control"}))
    genre = forms.CharField(required=False, widget=forms.TextInput({'placeholder': "Enter Song Genre",
                                                                    "class": "form-control"}))
    date = forms.CharField(required=False, widget=forms.TextInput({'placeholder': "Enter Song Date",
                                                                   "class": "form-control"}))
    cover = forms.FileField(required=False)

    # def clean_cover(self):
    #     """ Convert temp file to File object for easy use """
    #     return File(self.cleaned_data['cover'])
