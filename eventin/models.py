from django.db import models


class Event(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField(default=0, null=False,)

    def __str__(self):
        return self.name


class Participant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name
