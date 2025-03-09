from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms



attrs = {'class': 'form-control'}


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        label= 'Username',
        widget=forms.TextInput(attrs=attrs)
    )
    password = forms.CharField(
        label= 'Password',
        widget=forms.PasswordInput(attrs=attrs)
    )

class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(
        label= 'First Name',
        widget=forms.TextInput(attrs=attrs)
    )

    last_name = forms.CharField(
        label= 'Last Name',
        widget=forms.TextInput(attrs=attrs)
    )

    username = forms.CharField(
        label= 'Username',
        widget=forms.TextInput(attrs=attrs)
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs=attrs)
    )

    password1 = forms.CharField(
        label= 'Password',
        strip= False,
        widget=forms.PasswordInput(attrs=attrs)
    )

    password2 = forms.CharField(
        label= 'Password Confirmation',
        strip=False,
        widget=forms.PasswordInput(attrs=attrs)
    )

    class Meta(UserCreationForm.Meta):
        fields = ('first_name', 'last_name', 'username', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ProfileForm(UserChangeForm):
    password =  None

    class Meta:
        model= User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs=attrs),
            'last_name': forms.TextInput(attrs=attrs),
            'email': forms.EmailInput(attrs=attrs),
        }
