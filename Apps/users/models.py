from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

    followingList = models.ManyToManyField('self', related_name='followerList',symmetrical=False)
    def GetFollowingList(self):
        return "\n".join([p.username for p in self.followingList.all()])

    def GetFollowerList(self):
        return "\n".join([p.username for p in self.followerList.all()])


    GetFollowingList.short_description = 'Following'
    GetFollowerList.short_description = 'Follower'

