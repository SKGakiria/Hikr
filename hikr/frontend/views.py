from django.shortcuts import render, redirect
from events.models import Event
from groups.models import Group


def index(request):
    """
    Render the homepage/landing page of the application.
    """
    return render(request, 'index.html')


def groups_list(request):
    """
    Render list of groups.
    """
    return render(request, 'groups.html')


def events_list(request):
    """
    Render list of events.
    """
    return render(request, 'events.html')


def group(request, group_id):
    """
    Render group detail page with data direct from the database.
    Redirect to groups page if group does not exist.
    """
    try:
        group = Group.objects.get(pk=group_id)
        return render(request, 'group.html', {'group': group})
    except Group.DoesNotExist:
        return redirect('groups')

def event(request, event_id):
    """
    Render event detail page with data direct from the databse.
    Redirect to events page if event does not exist.
    """
    try:
        event = Event.objects.get(pk=event_id)
        return render(request, 'event.html', {'event': event})
    except Event.DoesNotExist:
        return redirect('events')


def sign_up(request):
    """
    Render sign up page.
    """
    return render(request, 'sign-up.html')


def login(request):
    """
    Render login page.
    """
    return render(request, 'login.html')