from django.urls import path

from . import views

urlpatterns = [
    path('', views.homeLoggin, name='homeLoggin'),
]