from django.shortcuts import render


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

def group(request):
    """
    Render group page.
    """
    return render(request, 'group.html')

def event(request):
    """
    Render event page.
    """
    return render(request, 'event.html')


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