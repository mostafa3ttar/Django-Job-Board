from django import forms
from users.models import User
from .models import Profile 
from django.contrib.auth.forms import UserCreationForm
from django_countries.widgets import CountrySelectWidget
from django.forms.widgets import Select



class SignForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
        
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['country','phone_number','image']









