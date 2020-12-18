from django.contrib import admin
from .models import Lisans42020
from .models import OnLisans2020

# Register your models here.
class Lisans42020Admin(admin.ModelAdmin):
    list_display = ('ProgramKodu', 'UniversiteAdi', 'FakulteAdi', 'BolumAdi', 'PuanTuru', 'GenelKontenjan','Yerlesen',
    'EnKucukPuan','EnBuyukPuan','OBKontenjan','OBYerlesen','OBEnKucukPuan','OBEnBuyukPuan')
    list_filter = ("ProgramKodu",)
    #list_display = ('ProgramKodu', 'UniversiteAdi')


admin.site.register(Lisans42020,Lisans42020Admin)

class OnLisans2020Admin(admin.ModelAdmin):
    list_display = ('ProgramKodu', 'UniversiteAdi', 'FakulteAdi', 'BolumAdi', 'PuanTuru', 'GenelKontenjan','Yerlesen',
    'EnKucukPuan','EnBuyukPuan','OBKontenjan','OBYerlesen','OBEnKucukPuan','OBEnBuyukPuan')
    list_filter = ("ProgramKodu",)
    #list_display = ('ProgramKodu', 'UniversiteAdi')


admin.site.register(OnLisans2020,OnLisans2020Admin)

# class Lisans42020Model(models.Model):
#    ProgramKodu = models.IntegerField()
#    UniversiteAdi = models.TextField()
#    FakulteAdi = models.TextField()
#    BolumAdi = models.TextField() 
#    PuanTuru = models.TextField()
#    GenelKontenjan = models.IntegerField()
#    Yerlesen = models.IntegerField()
#    EnKucukPuan = models.DecimalField(max_digits=10, decimal_places=4)
#    EnBuyukPuan = models.DecimalField(max_digits=10, decimal_places=4)
#    OBKontenjan = models.IntegerField()
#    OBYerlesen = models.IntegerField()
#    OBEnKucukPuan = models.DecimalField(max_digits=10, decimal_places=4)
#    OBEnBuyukPuan = models.DecimalField(max_digits=10, decimal_places=4)

# from django.contrib import admin
# from .models import Blog, Comment

# # Register your models here.
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('title','created_on')
#     list_filter = ("author",)
#     search_fields = ['title', 'body']
    
# class CommentAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('General information', {'fields': ['text', 'owner', 'likes', 'blog']}),
#         ('Date information', {'fields': ['created_time']}),
#         ('Edit information', {'fields': ['is_edited']}),
#     ]
#     list_display = ('text', 'owner', 'likes', 'created_time', 'is_edited')
#     list_filter = ['owner', 'likes', 'created_time', 'is_edited']
#     search_fields = ['text']

# admin.site.register(Blog, BlogAdmin)
# admin.site.register(Comment, CommentAdmin)