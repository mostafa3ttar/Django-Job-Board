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





















# class SignForm(forms.ModelForm):
    
#     country = forms.ChoiceField(
#         choices=[('', '---------')] + list(Profile._meta.get_field('country').choices),
#         widget=forms.Select(attrs={'class': 'form-control', 'size': '1'})
#     )
    
#     class Meta:
#         model = Profile
#         fields = '__all__'
#         # widgets = {
#         #     'country': CountrySelectWidget(attrs={'class': 'form-control custom-select'}),
#         # }
#         widgets = {
#             # التريك السحرية: إجبار الـ CountryField يلبس "بدلة" الـ Select الصغير
#             'country': Select(attrs={
#                 'class': 'form-control', 
#                 'size': '1', # ده السطر اللي بيمنعها تفرش كـ List
#                 'style': 'height: 40px !important;' # ده اللي بيجبر الطول
#             }),
#         }