from django.contrib import admin
from django.urls import path
from .views import delete_user
urlpatterns = [
    path('admin/', admin.site.urls),
    path('delete_user/', delete_user, name='delete_user'),
]
