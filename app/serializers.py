from rest_framework import serializers  
from app.models import Event

  
class EventSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Event
        fields = '__all__'
        many = True