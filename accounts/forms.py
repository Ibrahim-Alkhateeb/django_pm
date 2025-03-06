from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


attrs = {'class': 'form-control'}


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(attrs=attrs)
    )
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(attrs=attrs)
    )