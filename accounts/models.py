from django.db import models
from users.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django_countries import countries
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# class City(models.Model):
#     name = models.CharField(max_length=30)
    
#     def __str__(self):
#         return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=2, choices=countries, default='EG')
    phone_number = PhoneNumberField(blank=True, region=None)
    image = models.ImageField(upload_to='profile/')
    
    def __str__(self):
        return str(self.user)
    

## create new user --> create new empty profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)