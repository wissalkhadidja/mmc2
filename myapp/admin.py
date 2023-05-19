from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path
from django.shortcuts import render
from django.db.models import Q

from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')
    search_fields = ('username', 'email')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('search/', self.search_users, name='search_users'),
        ]
        return custom_urls + urls

    def search_users(self, request):
        if request.method == 'POST':
            search_query = request.POST.get('search_query')
            users = User.objects.filter(Q(username__icontains=search_query) | Q(email__icontains=search_query))
        else:
            users = User.objects.all()

        context = {
            'users': users,
            'search_query': search_query if request.method == 'POST' else '',
        }
        return render(request, 'admin/search_users.html', context)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Notification)
admin.site.register(UserProfile)
