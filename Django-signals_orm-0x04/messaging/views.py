from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login

@login_required
@csrf_exempt
def delete_user(request):
    if request.method == 'DELETE':
        user = request.user
        user.delete()
        return JsonResponse({'detail': 'User account deleted.'}, status=204)
    return JsonResponse({'detail': 'Method not allowed.'}, status=405)

@csrf_exempt
@require_POST
def api_login(request):
    import json
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'detail': 'Login successful.'})
    return JsonResponse({'detail': 'Invalid credentials.'}, status=400)