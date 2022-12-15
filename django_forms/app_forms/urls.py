from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_brigade', views.get_brigade, name='get_brigade'),
    path('get_facility', views.get_facility, name='get_facility'),
    path('get_info', views.get_info, name='get_info'),
] 