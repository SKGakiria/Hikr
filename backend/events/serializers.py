from rest_framework.serializers import HyperlinkedModelSerializer
from users.serializers import UserSerializer
from .models import Event, EventAttendance


class EventSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'url', 'name', 'description', 'location', 'difficulty', 'organizer', 'date', 'time', 'created_at', 'updated_at']


class EventAttendanceSerializer(HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = EventAttendance
        fields = ['id', 'joined_at', 'user']