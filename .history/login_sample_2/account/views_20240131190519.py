from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Event  # Eventモデルがあると仮定しています

@csrf_exempt
@require_http_methods(["POST"])
def add_event(request):
    try:
        data = json.loads(request.body)
        event = Event(title=data['title'], date=data['date'])
        event.save()
        return JsonResponse({'status': 'success', 'event': {'title': event.title, 'date': event.date}})
    except Exception as e:
        return JsonResponse({'status': 'error', 'error': str(e)}, status=400)
