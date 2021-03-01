from django import forms
from django.contrib.auth.models import User
from django.db.models import Q


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
