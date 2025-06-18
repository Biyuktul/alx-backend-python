from django.contrib import admin
from django.urls import include, path
from .views import api_login, delete_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('delete_user/', delete_user, name='delete_user'),
    path('api_login/', api_login, name='api_login'),
]
