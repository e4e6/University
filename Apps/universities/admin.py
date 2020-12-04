from django.contrib import admin
from .models import University, Faculty, Campus, Privilige, Department


class DepartmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'departmentType',]}),
        ('Points',               {'fields': ['puanType','minimumPuan','minimumRanking',]}),
    ]

class PriviligeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
    ]

class CampusAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
    ]

class FacultyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name','departmentList']}),
    ]
    filter_horizontal = ('departmentList',)


class UniversityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'info', 'detailedInfo']}),
        ('Student Information',               {'fields': ['numberOfLocalStudents', 'numberOfForeignStudents', 'universityType']}),
        ('Links',               {'fields': ['website_link', 'pinterest_link', 'twitter_link', 'instagram_link', 'linkedin_link', 'facebook_link']}),
        ('Photo Paths',               {'fields': ['profile_photo', 'cover_photo']}),
        ('Lists',               {'fields': ['facultyList','priviligeList','campusList']}),
    ]
    filter_horizontal = ('facultyList','priviligeList', 'campusList')
    list_display = ('name','info','GetEvents')

    # inlines = [FacultyInline]


admin.site.register(University, UniversityAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Campus, CampusAdmin)
admin.site.register(Privilige, PriviligeAdmin)
admin.site.register(Department, DepartmentAdmin)
