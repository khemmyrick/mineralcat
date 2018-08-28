from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mineral_list/', views.mineral_list, name='mineral_list'),
    path('random_mineral/', views.random_mineral, name='random_mineral'),
    path('mineral_detail/<pk>/', views.mineral_detail, name='mineral_detail'),
    path('group_list/<pk>', views.group_list, name='group_list'),
    path('random_ingroup/<pk>', views.random_ingroup, name='random_ingroup'),
]

# re_path(r'(?P<pk>\d+)/$', views.mineral_detail, name='mineral_detail'),

# path('mineral_detail/<pk>/', views.mineral_detail, name='mineral_detail'),
#     path('random_mineral/', views.random_mineral, name='random_mineral'),