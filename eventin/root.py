from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
@permission_classes([AllowAny])
def root(request):
    return Response({
        "message": "Welcome to Events API",
        "public_endpoints": {
            "events": reverse('event-list', request=request),
            "participants": reverse('participant-list', request=request),
        },
        "auth": {
            "user": "demo_user",
            "password": "Demo1234!",
            "token": reverse('token_obtain_pair', request=request),
            "refresh": reverse('token_refresh', request=request),
        }
    })
