from .models import Event, Participant, Registration
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser
from .serializers import (
    EventSerializer, ParticipantSerializer, RegistrationSerializer,
    ListRegistrationEventSerializer, ListRegistrationParticipantSerializer,
    ParticipantSerializerV2
)


class EventViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'location',]


class ParticipantViewset(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'cpf',]

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return ParticipantSerializerV2
        return ParticipantSerializer


class RegistrationViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['event', 'participant', 'date_registered']
    search_fields = ['event', 'participant', 'date_registered',]


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
