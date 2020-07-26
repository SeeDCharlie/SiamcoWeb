from django.urls import path

from . import views

urlpatterns = [
    path('', views.homeLoggin, name = 'homeLoggin'),
    path('generate-cot', views.mainCot, name = 'mainCot'),
]