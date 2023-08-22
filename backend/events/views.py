from django.shortcuts import get_object_or_404
from rest_framework import generics, status, serializers, permissions
from rest_framework.exceptions import MethodNotAllowed, NotFound
from rest_framework.response import Response
from groups.permissions import IsOwnerOrReadOnly
from .models import Event, EventAttendance
from .serializers import EventSerializer, EventAttendanceSerializer


class EventListCreateView(generics.ListCreateAPIView):
    """
    List all events, or create a new event.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EventRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an event instance.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class EventAttendanceListCreateView(generics.ListCreateAPIView):
    """
    List all event attendees, or create a new event attendee/participant.
    """
    serializer_class = EventAttendanceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        event_id = self.kwargs['pk']
        return EventAttendance.objects.filter(event_id=event_id)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        elif not queryset.exists():
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response([])
        
    def perform_create(self, serializer):
        event_id = self.kwargs['pk']
        user = self.request.user
        event = get_object_or_404(Event, pk=event_id)

        # Check if the user is already a participant of the event
        if event.attendees.filter(user=user).exists():
            raise serializers.ValidationError("User is already a participant of this event.")

        serializer.save(user=user, event=event)


class EventAttendanceDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Delete an event attendee/participant.
    Retrieve and update are not allowed.
    """
    queryset = EventAttendance.objects.all()
    serializer_class = EventAttendanceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def delete(self, *args, **kwargs):
        event_id = self.kwargs['pk']
        user_id = self.kwargs['participant_pk']

        try:
            event_attendance = EventAttendance.objects.get(event_id=event_id, user_id=user_id)
        except EventAttendance.DoesNotExist:
            raise NotFound("Event participant does not exist.")
        
        event_attendance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)
    
    def put(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)