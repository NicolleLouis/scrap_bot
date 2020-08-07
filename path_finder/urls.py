from django.urls import path

from path_finder import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analyse_url', views.analyse_url, name='analyse_url'),
    path('display_classes', views.display_classes, name='display_classes'),
]
