from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from events.models import Event, EventAttendance
from groups.models import Group, GroupMembership


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
        membership = False
        if request.user.is_authenticated:
            membership = GroupMembership.objects.filter(group_id=group_id, user=request.user).exists()
        return render(request, 'group.html', {'group': group, 'membership': membership})
    except Group.DoesNotExist:
        return redirect('groups')


@login_required
def join_group(request, group_id):
    """
    Join a group.
    """
    if request.method == 'POST':
        group = Group.objects.get(pk=group_id)
        GroupMembership.objects.create(group=group, user=request.user)
        return redirect('group-detail', group_id=group_id)
    
    return redirect('group-detail', group_id=group_id)


@login_required
def leave_group(request, group_id):
    """
    Leave a group.
    """
    if request.method == 'POST':
        group = Group.objects.get(pk=group_id)
        GroupMembership.objects.filter(group=group, user=request.user).delete()
        return redirect('group-detail', group_id=group_id)

    return redirect('group-detail', group_id=group_id)


def event(request, event_id):
    """
    Render event detail page with data direct from the databse.
    Redirect to events page if event does not exist.
    """
    try:
        event = Event.objects.get(pk=event_id)
        attendance = False
        if request.user.is_authenticated:
            attendance = EventAttendance.objects.filter(event_id=event_id, user=request.user).exists()
        return render(request, 'event.html', {'event': event, 'attendance': attendance})
    except Event.DoesNotExist:
        return redirect('events')


@login_required
def join_event(request, event_id):
    """
    Attend an event.
    """
    if request.method == 'POST':
        event = Event.objects.get(pk=event_id)
        EventAttendance.objects.create(event=event, user=request.user)
        return redirect('event-detail', event_id=event_id)
    
    return redirect('event-detail', event_id=event_id)


@login_required
def leave_event(request, event_id):
    """
    Unattend an event.
    """
    if request.method == 'POST':
        event = Event.objects.get(pk=event_id)
        EventAttendance.objects.filter(event=event, user=request.user).delete()
        return redirect('event-detail', event_id=event_id)

    return redirect('event-detail', event_id=event_id)


def sign_up(request):
    """
    Render sign up page.
    """
    if request.user.is_authenticated:
        return redirect('index')
    return render(request, 'sign-up.html')


def login(request):
    """
    Render login page.
    """
    if request.user.is_authenticated:
        return redirect('index')
    return render(request, 'login.html')

def logout_view(request):
    """
    Log user out and redirect to homepage.
    """
    logout(request)
    return redirect('login')


def check_auth(request):
    """
    Check if user is authenticated.
    """
    return JsonResponse({'is_authenticated': request.user.is_authenticated})

def about(request):
    """
    Render about page.
    """
    return render(request, 'about.html')