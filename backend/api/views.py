from rest_framework import generics
from rest_framework.filters import SearchFilter
from events.models import Event
from events.serializers import EventSerializer
from groups.models import Group
from groups.serializers import GroupSerializer


class GroupSearchView(generics.ListAPIView):
    """
    Search for groups by name, location, or description.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'location', 'description']

class EventSearchView(generics.ListAPIView):
    """
    Search for events by name, location, date, or description.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [SearchFilter]
    search_fields = [ 'name', 'location', 'date', 'description']
