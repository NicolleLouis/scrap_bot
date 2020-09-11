from django.urls import path

from path_finder import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analyse_url', views.analyse_url, name='analyse_url'),
    path('display_classes', views.display_classes, name='display_classes'),
    path('class_detail', views.display_detail_class, name='display_detail_class'),
    path('display_links', views.display_links, name='display_links'),
    path('is_link_recursive', views.is_link_recursive, name='is_link_recursive'),
]
