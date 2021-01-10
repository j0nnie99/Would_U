from django.contrib import admin
from .models import Community,Scrap
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Community)
admin.site.register(Scrap)