from django.contrib import admin
from django.urls import path,include
from .  import views


urlpatterns = [
    path('device-detail/',views.device_detail, name='device_detail'),
    path('device-list/',views.device_list, name='device_list'),
    path('device-edit/',views.device_edit, name='device_edit')

]
