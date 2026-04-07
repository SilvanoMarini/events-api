import random
from django.core.management.base import BaseCommand
from eventin.models import Event, Participant, Registration
from faker import Faker


class Command(BaseCommand):
    help = 'Populate the database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker('pt_BR')
        population_size = 40

        # Clear existing data to avoid duplication during population (development only)
        Registration.objects.all().delete()
        Participant.objects.all().delete()
        Event.objects.all().delete()

        events_names = [
            'Python Workshop',
            'Django Conference',
            'React Workshop',
            'Angular Conference',
            'Vue Conference',
            'Flutter Conference',
            'Go Conference',
            'Java Conference',
            'Kotlin Conference',
            'Swift Conference',
            'Rust Conference',
            'C# Conference',
            'C++ Conference',
            'C Conference',
        ]

        events_list = []

        for event_name in events_names:
            event = Event(
                name=event_name,
                description=fake.text(max_nb_chars=200),
                date=fake.date_time_between(
                    start_date="+1d", end_date="+30d"),
                location=fake.city(),
                capacity=random.randint(50, 200),
            )
            events_list.append(event)

        Event.objects.bulk_create(events_list)

        used_cpfs = set()
        used_emails = set()
        used_phones = set()
        participants_list = []

        # Ensure unique CPF, email, and phone for each participant
        for _ in range(population_size):
            while True:
                cpf = fake.cpf()
                email = fake.email()
                phone = fake.msisdn()

                if cpf not in used_cpfs and email not in used_emails and phone not in used_phones:
                    used_cpfs.add(cpf)
                    used_emails.add(email)
                    used_phones.add(phone)
                    break

            participants_list.append(Participant(
                name=fake.name(),
                cpf=cpf,
                email=email,
                phone=phone,
            ))

        Participant.objects.bulk_create(participants_list)

        events = list(Event.objects.all())
        participants = list(Participant.objects.all())

        # Create random registrations linking participants to events
        for _ in range(100):
            event = random.choice(events)
            participant = random.choice(participants)
            Registration.objects.get_or_create(
                event=event, participant=participant)
