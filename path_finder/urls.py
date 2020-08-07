from django.urls import path

from path_finder import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analyse_url', views.analyse_url, name='analyse_url'),
]
