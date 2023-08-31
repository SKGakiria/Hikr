from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('groups/', views.groups_list, name='groups'),
    path('events/', views.events_list, name='events'),
    path('group/', views.group, name='group'),
    path('event/', views.event, name='event'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('login/', views.login, name='login'),
]