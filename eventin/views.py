from .models import Event, Participant, Registration
from rest_framework import viewsets
from .serializers import EventSerializer, ParticipantSerializer, RegistrationSerializer


class EventViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ParticipantViewset(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class RegistrationViewset(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
