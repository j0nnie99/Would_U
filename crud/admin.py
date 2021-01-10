from django.contrib import admin
from .models import Post, Join, Like
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Post)
admin.site.register(Join)
admin.site.register(Like)