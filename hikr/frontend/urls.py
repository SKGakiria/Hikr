from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('groups/', views.groups_list, name='groups'),
    path('events/', views.events_list, name='events'),
    path('groups/<int:group_id>/', views.group, name='group-detail'),
    path('groups/<int:group_id>/join/', views.join_group, name='join-group'),
    path('groups/<int:group_id>/leave/', views.leave_group, name='leave-group'),
    path('events/<int:event_id>', views.event, name='event-detail'),
    path('events/<int:event_id>/join/', views.join_event, name='join-event'),
    path('events/<int:event_id>/leave/', views.leave_event, name='leave-event'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
]