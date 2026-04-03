from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator
from .validators import validate_cpf, validate_name, validate_phone
import re


class Event(models.Model):
    name = models.CharField(max_length=200, validators=[MinLengthValidator(3)])
    description = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateTimeField()
    location = models.CharField(max_length=200, validators=[
                                MinLengthValidator(3)])
    capacity = models.PositiveIntegerField(
        default=0, null=False)
    participant = models.ManyToManyField(
        'Participant', through='Registration', related_name='events')

    def __str__(self):
        return self.name


class Participant(models.Model):
    name = models.CharField(max_length=200, validators=[
        validate_name])
    cpf = models.CharField(max_length=14, unique=True,
                           validators=[validate_cpf])
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    phone = models.CharField(max_length=16, unique=True, validators=[
                             validate_phone])

    def __str__(self):
        return self.name

# Normalize CPF to store only numbers in the database
    def save(self, *args, **kwargs):
        if self.cpf:
            self.cpf = re.sub(r'\D', '', self.cpf)
        super().save(*args, **kwargs)


class Registration(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='registrations')
    participant = models.ForeignKey(
        Participant, on_delete=models.CASCADE, related_name='registrations')
    date_registered = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['event', 'participant'], name='unique_registration')]

    def __str__(self):
        return f"{self.event.name} - {self.participant.name}"
