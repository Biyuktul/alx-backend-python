from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, logout
from django.shortcuts import redirect
from django.http import HttpResponse

User = get_user_model()

@login_required
def delete_user(request):
    user = request.user
    logout(request)
    user.delete()
    return HttpResponse("Your account has been deleted.")