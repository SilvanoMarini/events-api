from django.contrib import admin
from django.urls import path, include
from eventin.views import EventViewset, ParticipantViewset, RegistrationViewset, ListRegistrationEventViewset, ListRegistrationParticipantViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'events', EventViewset)
router.register(r'participants', ParticipantViewset)
router.register(r'registrations', RegistrationViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('events/<int:pk>/registrations',
         ListRegistrationEventViewset.as_view()),
    path('participants/<int:pk>/registrations',
         ListRegistrationParticipantViewset.as_view()),
]
