from django.contrib import admin

# Register your models here.

from .models import Post


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General information', {'fields': ['text', 'owner', 'likes']}),
        ('Date information', {'fields': ['created_time']}),
        ('Edit information', {'fields': ['is_edited']}),
    ]
    list_display = ('text', 'owner', 'likes', 'created_time', 'is_edited')
    list_filter = ['owner', 'likes', 'created_time', 'is_edited']
    search_fields = ['text']

admin.site.register(Post, PostAdmin)

