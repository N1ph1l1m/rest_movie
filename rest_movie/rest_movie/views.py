from django.http import JsonResponse


def request_status_view(request):
    status_code = request.status_code  # Получаем статус запроса
    return JsonResponse({'status_code': status_code})