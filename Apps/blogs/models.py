
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.timezone import now


class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        #get_user_model(),
        #'auth.User',
        settings.AUTH_USER_MODEL,
        
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    #date = models.DateTimeField(auto_now_add=True,blank=True)   önceden vardı
    ##date = models.DateTimeField(default=now, editable=False)   sonra yaptım

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title   # burda primary key mi yaptı yani aynı başlıkta 2 post olmazmı ?

    def get_absolute_url(self): 
        return reverse('blogs:makale_detail', args=[str(self.id)])


class Comment(models.Model):
    text = models.CharField(max_length=200)
    created_time = models.DateTimeField('date published')
    is_edited = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='commentList', on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.text
