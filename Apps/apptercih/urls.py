# pages/urls.py
from django.urls import path
from .views import HomePageView
from . import views
app_name = 'apptercih'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('tyt_hesaplama',views.tyt_hesaplama,name="tyt_hesaplama"),

    

]
