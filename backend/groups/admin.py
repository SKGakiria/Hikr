from django.contrib import admin
from .models import Group, GroupMembership


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_per_page = 25


class GroupMembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'user', 'joined_at')
    list_display_links = ('id', 'group')
    search_fields = ('group', 'user')
    list_per_page = 25


admin.site.register(Group, GroupAdmin)
admin.site.register(GroupMembership, GroupMembershipAdmin)