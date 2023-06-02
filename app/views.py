from django.shortcuts import render
from rest_framework.response import Response
from app import models, serializers
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView
# Create your views here.

class EventGetRecentView(ListAPIView):
    def get(self, request):
        # Fetch the most recent event
        event = models.Event.objects.order_by('schedule').first()
        serializer = serializers.EventSerializer([event], many=True)
        return Response(serializer.data)
    serializer_class = serializers.EventSerializer

class EventGetView(RetrieveAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

class EventCreateView(CreateAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

class EventUpdateView(UpdateAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

class EventDeleteView(DestroyAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
