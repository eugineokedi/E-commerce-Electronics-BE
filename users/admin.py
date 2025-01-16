from django.contrib import admin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'date_joined')
    search_fields = ('email')
    ordering = ('-date_joined',)