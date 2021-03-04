from django import forms


class CropForm(forms.Form):
    """ Form parameters to crop an audio file """
    minute = forms.IntegerField(required=True, min_value=0, max_value=9)
    seconds = forms.IntegerField(required=True, min_value=0, max_value=59)
    length = forms.IntegerField(required=True, min_value=0, max_value=59)






