from rest_framework import serializers
from .models import Event, Participant, Registration


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'date', 'location', 'capacity']
        read_only_fields = ['id']


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'name', 'cpf', 'email', 'phone']
        read_only_fields = ['id']


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'event', 'participant', 'date_registered']
        read_only_fields = ['id']
