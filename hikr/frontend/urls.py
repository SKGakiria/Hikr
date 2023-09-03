from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('groups/', views.groups_list, name='groups'),
    path('events/', views.events_list, name='events'),
    path('groups/<int:group_id>/', views.group, name='group-detail'),
    path('events/<int:event_id>', views.event, name='event-detail'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('login/', views.login, name='login'),
]