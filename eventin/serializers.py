from rest_framework import serializers
from .models import Event, Participant, Registration
from django.utils import timezone
from django.db import transaction
from .validators import validate_cpf, validate_name, validate_phone


class EventSerializer(serializers.ModelSerializer):
    remaining_capacity = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'date',
                  'location', 'capacity', 'remaining_capacity']
        read_only_fields = ['id']

    def get_remaining_capacity(self, obj):
        return obj.capacity - obj.registrations.count()

    def validate_name(self, value):
        value = value.strip()
        if len(value) < 3:
            raise serializers.ValidationError(
                "Name must have at least 3 characters.")

        return value

    def validate_description(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError(
                "Description must have at least 10 characters.")
        return value.strip()

    def validate_date(self, value):
        # Skip validation if the date remains unchanged during update operations
        if self.instance and value == self.instance.date:
            return value

        if value < timezone.now():
            raise serializers.ValidationError("Date cannot be in the past.")

        return value

    def validate_location(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Location must have at least 3 characters.")
        return value.strip()

    def validate_capacity(self, value):
        if value < 1:
            raise serializers.ValidationError("Capacity must be at least 1.")
        return value


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'name', 'cpf', 'email', 'phone',]
        read_only_fields = ['id']

    def validate_name(self, value):
        return validate_name(value)

    def validate_cpf(self, value):
        if self.instance and value == self.instance.cpf:
            return value
        return validate_cpf(value)

    def validate_phone(self, value):
        if self.instance and value == self.instance.phone:
            return value
        return validate_phone(value)


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'event', 'participant', 'date_registered']
        read_only_fields = ['id']

    def validate(self, data):
        event = data['event']

        total_registrations = event.registrations.count()

        if total_registrations >= event.capacity:
            raise serializers.ValidationError(
                "This event has reached maximum capacity."
            )

        return data

    def create(self, validated_data):
        with transaction.atomic():
            event = validated_data['event']

            # Lock the event row to ensure capacity check is consistent
            # and prevent overbooking in concurrent transactions
            event = Event.objects.select_for_update().get(id=event.id)

            if event.registrations.count() >= event.capacity:
                raise serializers.ValidationError(
                    "This event has reached maximum capacity."
                )

        return super().create(validated_data)


class ListRegistrationEventSerializer(serializers.ModelSerializer):
    participant = serializers.StringRelatedField()

    class Meta:
        model = Registration
        fields = ['participant', 'date_registered']


class ListRegistrationParticipantSerializer(serializers.ModelSerializer):
    event = serializers.StringRelatedField()

    class Meta:
        model = Registration
        fields = ['event', 'date_registered']
