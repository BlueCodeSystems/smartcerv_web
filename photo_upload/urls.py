from django.urls import path
from django.contrib import admin

from . import views

app_name = 'photo_upload'
urlpatterns = [
    path('', admin.site.urls),
]