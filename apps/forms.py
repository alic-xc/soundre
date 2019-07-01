from django import forms

class TagViewForm(forms.Form):
    
    audio = forms.FileField(widget = forms.FileInput({'accept':'.mp3'}))


class TagEditForm(forms.Form):
    pass

