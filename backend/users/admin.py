from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active', 'date_joined', 'last_login')
    list_display_links = ('id', 'username')
    search_fields = ('username', 'email')
    list_per_page = 25


admin.site.register(User, UserAdmin)