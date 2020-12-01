from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Subscribers


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username','email','GetFollowingList','GetFollowerList')
    fieldsets = UserAdmin.fieldsets + (('Additional infos', {'fields': ('age','followingList', )}),)
    filter_horizontal = ('followingList',)

class SubscribersAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['email', 'createdTime', 'is_active']}),
    ]
    readonly_fields = ['createdTime']
    list_display = ('email','createdTime','is_active')



admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Subscribers, SubscribersAdmin)
