from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mineral_list/', views.mineral_list, name='mineral_list'),
    path('random_mineral/', views.random_mineral, name='random_mineral'),
    path('mineral_detail/<pk>/', views.mineral_detail, name='mineral_detail'),
]

# re_path(r'(?P<pk>\d+)/$', views.mineral_detail, name='mineral_detail'),

# path('mineral_detail/<pk>/', views.mineral_detail, name='mineral_detail'),
#     path('random_mineral/', views.random_mineral, name='random_mineral'),