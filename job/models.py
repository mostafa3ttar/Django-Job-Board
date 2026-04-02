from django.db import models
import uuid
from django.utils.text import slugify

from users.models import User

# Create your models here.

"""
Django Model Field :
    - html widget
    - Validation
    - DB size


"""

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)


class Job(models.Model):  #Class => Table
    owner = models.ForeignKey(User, related_name='job_owner' ,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  # Column
    #location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)    # ONE TO MANY
    exprience = models.IntegerField(default=1)
    img = models.ImageField(upload_to='jobs_img/%y%m%d', null=True, blank=True)
    
    slug = models.SlugField(null=True, blank=True, unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            original_slug = slugify(self.title)    ##logic
            self.slug = f"{original_slug}-{str(uuid.uuid4())[:4]}"
        super(Job,self).save(*args, **kwargs)
        
    
    
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    
    
class Apply(models.Model):
    job = models.ForeignKey(Job, verbose_name=("job_apply"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    website = models.URLField(max_length=200)
    cv = models.FileField(upload_to='apply/%y%m%d')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name