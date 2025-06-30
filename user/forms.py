from django import forms
from django.forms.models import ModelForm
from user.models import User

class UserFormLogin(ModelForm):
    class Meta:
        model = User
        fields = ['user_name','password']
        widgets = {
            'password': forms.PasswordInput(),
        }
