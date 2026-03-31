from django.http import JsonResponse
from .models import Event, Participant
from rest_framework import viewsets
from .serializers import EventSerializer, ParticipantSerializer


class EventViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ParticipantViewset(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
