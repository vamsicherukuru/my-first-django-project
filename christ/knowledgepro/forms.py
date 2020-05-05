from django.contrib.auth.models import User
from django import forms
from knowledgepro.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')


class UserDetailsForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('display_pic','linkedIn_url')
        
