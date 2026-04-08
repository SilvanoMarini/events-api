from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from eventin.health import health
from eventin.root import root
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from eventin.views import (
    EventViewset, ParticipantViewset, RegistrationViewset,
    ListRegistrationEventViewset, ListRegistrationParticipantViewset,
)


router = routers.DefaultRouter()
router.register(r'events', EventViewset)
router.register(r'participants', ParticipantViewset)
router.register(r'registrations', RegistrationViewset)

urlpatterns = [
    # System / Infrastructure
    path('health/', health, name='health'),
    path('admin/', admin.site.urls),

    # Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Main API
    path('api/', include(router.urls)),

    # Root
    path('', root, name='root'),

    # Relationships
    path(
        'api/events/<int:pk>/registrations/',
        ListRegistrationEventViewset.as_view(),
        name='event-registrations'
    ),
    path(
        'api/participants/<int:pk>/registrations/',
        ListRegistrationParticipantViewset.as_view(),
        name='participant-registrations'
    ),
]
