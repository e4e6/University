from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username','email','GetFollowingList','GetFollowerList')
    fieldsets = UserAdmin.fieldsets + (('Additional infos', {'fields': ('age','followingList', )}),)
    filter_horizontal = ('followingList',)


admin.site.register(CustomUser, CustomUserAdmin)
