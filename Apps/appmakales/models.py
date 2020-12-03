
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.


# class Makale(models.Model):
#     text = models.CharField(max_length=200)
#     created_time = models.DateTimeField('date published')
#     is_edited = models.BooleanField(default=False)
#     owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     likes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.text

class Makale(models.Model):
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

    def get_absolute_url(self) : 
        return reverse('appmakales:makale_detail', args=[str(self.id)])