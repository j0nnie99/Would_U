from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Community(models.Model):
    title = models.CharField('제목',max_length=200)
    username = models.ForeignKey(User, related_name='communities', on_delete=models.CASCADE)
    pub_date = models.DateTimeField('날짜',auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    body = models.TextField('본문')
    scrap_user_set = models.ManyToManyField(User, related_name='scrap_user_set', through='Scrap')
    view_count = models.IntegerField(default=0)
    scrap_counting = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def scrap_count(self):
        return self.scrap_user_set.count()

class Scrap(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Community, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
     
