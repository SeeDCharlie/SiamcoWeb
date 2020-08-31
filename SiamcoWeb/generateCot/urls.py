from django.urls import path

from . import views

urlpatterns = [
    path('', views.homeLoggin, name = 'homeLoggin'),
    path('generate-cot', views.mainCot, name = 'mainCot'),
    path('predocument', views.genCot, name = 'genCot'),
    path('document', views.docCotHtml, name = 'modelCot'),
    path('saveActi', views.saveActiviti, name = 'saveActi'),
    path('<str:username>/manage_activities', views.manageActivities, name = 'manageActivities'),
    #ath('document', views.HelloPDFView.as_view(), name = 'modelCot'),
]