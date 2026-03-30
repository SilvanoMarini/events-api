from django.contrib import admin
from eventin.models import Event, Participant


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
