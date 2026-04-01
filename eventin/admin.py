from django.contrib import admin
from eventin.models import Event, Participant, Registration


class Events(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'location', 'capacity')
    list_filter = ('name', 'date',)
    search_fields = ('name', 'description', 'location')
    ordering = ('id', 'name')
    list_per_page = 20


admin.site.register(Event, Events)


class Participants(admin.ModelAdmin):
    list_display = ('id', 'name', 'cpf', 'email', 'phone')
    list_filter = ('name', 'cpf', 'email', 'phone')
    search_fields = ('name', 'cpf', 'email', 'phone')
    ordering = ('id', 'name')
    list_per_page = 20


admin.site.register(Participant, Participants)


class Registrations(admin.ModelAdmin):
    list_display = ('id', 'event', 'participant', 'date_registered')
    list_filter = ('event', 'participant', 'date_registered')
    search_fields = ('event', 'participant', 'date_registered')
    ordering = ('id',)
    list_per_page = 20


admin.site.register(Registration, Registrations)
