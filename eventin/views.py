from django.http import JsonResponse


def participants(request):
    if request.method == 'GET':
        participants = {
            'id': 1,
            'name': 'John Doe',
        }

    return JsonResponse(participants)
