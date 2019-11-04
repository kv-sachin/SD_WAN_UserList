# -*- coding: utf-8 -*-

from django.contrib import admin
from user.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['ID', 'User_name', 'Company', 'City', 'DATE', 'Device_Serial_Number']
    
admin.site.register(User, UserAdmin)