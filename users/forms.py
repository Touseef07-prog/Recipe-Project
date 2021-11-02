from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm,
)





class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'main-input-box'
        self.fields['email'].widget.attrs['class'] = 'main-input-box'
        self.fields['password1'].widget.attrs['class'] = 'main-input-box'
        self.fields['password2'].widget.attrs['class'] = 'main-input-box'

    class Meta:
        model = User
        fields = ('email', 'username','password1', 'password2')


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'main-input-box'
        self.fields['password'].widget.attrs['class'] = 'main-input-box'
    class Meta:
        model = User
        fields = ('username','password1')