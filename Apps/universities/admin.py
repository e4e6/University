from django.contrib import admin
from .models import University, Faculty, Department

# Register your models here.

class FacultyInline(admin.StackedInline):
    model = Faculty
    extra = 1

class DepartmentInline(admin.StackedInline):
    model = Department
    extra = 1

class DepartmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'faculty']}),
    ]

class FacultyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'university']}),
    ]
    inlines = [DepartmentInline]

class UniversityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'info']}),
        ('Student Information',               {'fields': ['numberOfLocalStudents', 'numberOfForeignStudents', 'universityType']}),
        # ('Links',               {'fields': ['website_link', 'pinterest_link', 'twitter_link', 'instagram_link', 'linkedin_link', 'facebook_link']}),
        ('Links',               {'fields': ['website_link',]}),
        ('Photo Paths',               {'fields': ['profile_photo_path', 'cover_photo_path']}),
    ]
    inlines = [FacultyInline]


admin.site.register(University, UniversityAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Department, DepartmentAdmin)

# admin.site.register(University, UniversityAdmin)
# admin.site.register(Faculty, FacultyAdmin)
# admin.site.register(Department, DepartmentAdmin)