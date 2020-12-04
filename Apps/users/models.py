from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

    followingList = models.ManyToManyField('self', related_name='followerList',symmetrical=False,  blank=True)
    def GetFollowingList(self):
        return "\n".join([p.username for p in self.followingList.all()])

    def GetFollowerList(self):
        return "\n".join([p.username for p in self.followerList.all()])


    GetFollowingList.short_description = 'Following'
    GetFollowerList.short_description = 'Follower'

class Subscribers(models.Model):
    email = models.EmailField(max_length=200)
    is_active = models.BooleanField(default=True)
    createdTime = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Subscribers"
