from django.contrib import admin
from django.urls import path
from eventin.views import participants

urlpatterns = [
    path('admin/', admin.site.urls),
    path('participants/', participants),
]
