from django.contrib import admin
from .models import Blog, Comment

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','created_on')
    list_filter = ("author",)
    search_fields = ['title', 'body']
    
class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General information', {'fields': ['text', 'owner', 'likes', 'blog']}),
        ('Date information', {'fields': ['created_time']}),
        ('Edit information', {'fields': ['is_edited']}),
    ]
    list_display = ('text', 'owner', 'likes', 'created_time', 'is_edited')
    list_filter = ['owner', 'likes', 'created_time', 'is_edited']
    search_fields = ['text']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
