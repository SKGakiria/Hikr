from django.urls import path
from users.views import UserListCreateView, UserRetrieveUpdateDeleteView
from groups.views import GroupListCreateView, GroupRetrieveUpdateDeleteView, GroupMembershipListCreateView, GroupMembershipDeleteView
from events.views import EventListCreateView, EventRetrieveUpdateDeleteView, EventAttendanceListCreateView, EventAttendanceDeleteView
from .views import GroupSearchView, EventSearchView

urlpatterns = [
    path('groups/', GroupListCreateView.as_view(), name='group-list'),
    path('groups/<int:pk>/', GroupRetrieveUpdateDeleteView.as_view(), name='group-detail'),
    path('groups/<int:pk>/members/', GroupMembershipListCreateView.as_view(), name='group-membership-list'),
    path('groups/<int:pk>/members/<int:member_pk>/', GroupMembershipDeleteView.as_view(), name='group-membership-delete'),
    path("events/", EventListCreateView.as_view(), name="event-list"),
    path("events/<int:pk>/", EventRetrieveUpdateDeleteView.as_view(), name="event-detail"),
    path("events/<int:pk>/participants/", EventAttendanceListCreateView.as_view(), name="api-event-participants-list"),
    path("events/<int:pk>/participants/<int:participant_pk>/", EventAttendanceDeleteView.as_view(), name="event-participants-detail"),
    path("users/", UserListCreateView.as_view(), name="user-list"),
    path("users/<int:pk>/", UserRetrieveUpdateDeleteView.as_view(), name="user-detail"),
]