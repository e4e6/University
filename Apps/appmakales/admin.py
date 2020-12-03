from django.contrib import admin
from .models import Makale

# Register your models here.
class MakaleAdmin(admin.ModelAdmin):
    list_display = ('title','created_on')
    list_filter = ("author",)
    search_fields = ['title', 'body']
    

admin.site.register(Makale, MakaleAdmin)