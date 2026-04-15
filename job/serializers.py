### get data from model ---> json 
from rest_framework import routers, serializers, viewsets
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'