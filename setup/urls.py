from django.contrib import admin
from django.urls import path, include
from eventin.views import EventViewset, ParticipantViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'events', EventViewset)
router.register(r'participants', ParticipantViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
