from django.urls import path
from users.views import UserListView, UserRetrieveUpdateDeleteView, UserRegisterView, LoginView
from groups.views import GroupListCreateView, GroupRetrieveUpdateDeleteView, GroupMembershipListCreateView, GroupMembershipDeleteView
from events.views import EventListCreateView, EventRetrieveUpdateDeleteView, EventAttendanceListCreateView, EventAttendanceDeleteView
from .views import api_root
from knox import views as knox_views

urlpatterns = [
    path('', api_root, name='api-root'),
    path('groups/', GroupListCreateView.as_view(), name='group-list'),
    path('groups/<int:pk>/', GroupRetrieveUpdateDeleteView.as_view(), name='group-detail'),
    path('groups/<int:pk>/members/', GroupMembershipListCreateView.as_view(), name='group-membership-list'),
    path('groups/<int:pk>/members/<int:member_pk>/', GroupMembershipDeleteView.as_view(), name='group-membership-delete'),
    path("events/", EventListCreateView.as_view(), name="event-list"),
    path("events/<int:pk>/", EventRetrieveUpdateDeleteView.as_view(), name="event-detail"),
    path("events/<int:pk>/participants/", EventAttendanceListCreateView.as_view(), name="api-event-participants-list"),
    path("events/<int:pk>/participants/<int:participant_pk>/", EventAttendanceDeleteView.as_view(), name="event-participants-delete"),
    path("users/", UserListView.as_view(), name="user-list"),
    path("users/<int:pk>/", UserRetrieveUpdateDeleteView.as_view(), name="user-detail"),
    path("users/register/", UserRegisterView.as_view(), name="user-register"),
    path("users/login/", LoginView.as_view(), name="knox_login"),
    path("users/logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path("users/logoutall/", knox_views.LogoutAllView.as_view(), name="knox_logoutall"),
]