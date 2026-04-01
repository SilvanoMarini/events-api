from .models import Event, Participant, Registration
from rest_framework import viewsets, generics
from .serializers import (
    EventSerializer, ParticipantSerializer, RegistrationSerializer, ListRegistrationEventSerializer, ListRegistrationParticipantSerializer
)


class EventViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ParticipantViewset(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class RegistrationViewset(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class ListRegistrationEventViewset(generics.ListAPIView):
    serializer_class = ListRegistrationEventSerializer

    def get_queryset(self):
        event_id = self.kwargs['pk']
        return Registration.objects.filter(event_id=event_id)


class ListRegistrationParticipantViewset(generics.ListAPIView):
    serializer_class = ListRegistrationParticipantSerializer

    def get_queryset(self):
        participant_id = self.kwargs['pk']
        return Registration.objects.filter(participant_id=participant_id)
