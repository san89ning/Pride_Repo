from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Userprofile

class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ['first_name', 'last_name', 'address', 'gender', 'profile_image']
