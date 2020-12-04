from django.contrib import admin
from .models import Event
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name','text','color']}),
        ('Date',               {'fields': ['startDate','endDate']}),
        ('University',               {'fields': ['university',]}),
    ]


admin.site.register(Event, EventAdmin)
