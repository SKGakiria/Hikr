from django.contrib import admin
from .models import Event, EventAttendance


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'time', 'location', 'description', 'created_at', 'updated_at')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'group', 'location', 'description')
    list_per_page = 25


class EventAttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'user', 'joined_at')
    list_display_links = ('id', 'event')
    search_fields = ('event', 'user')
    list_per_page = 25


admin.site.register(Event, EventAdmin)
admin.site.register(EventAttendance, EventAttendanceAdmin)