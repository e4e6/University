from django.urls import path
from .views import HomePageView
from . import views

app_name = 'apptercihrobotu'
urlpatterns = [
    path('', HomePageView.as_view(), name='home_tercihrobotu'),
    #path('tyt_hesaplama',views.tyt_hesaplama,name="tyt_hesaplama"),
    #path('Sonuc/',views.secim,name='sonuc_tercihrobotu'),
    #path('',views.AlanAzaltma,name='home_tercihrobotu'),
    path('sonuchesapla/',views.alanAzaltma,name='sonuchesapla'),
    #path('searchuni/',views.searchuni,name='searchuni'),
]