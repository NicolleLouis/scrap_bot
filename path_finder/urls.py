from django.urls import path

from path_finder import views

urlpatterns = [
    path('', views.home, name='home'),
]
