from django.db import models
from django.conf import settings
# Create your models here.


class Post(models.Model):
    text = models.CharField(max_length=200)
    created_time = models.DateTimeField('date published')
    is_edited = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.text
