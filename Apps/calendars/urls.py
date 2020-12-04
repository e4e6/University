from django.urls import path

from . import views

app_name = 'calendars'
urlpatterns = [
    path('', views.index, name='index'),
    path('getEvents/', views.getEvents, name='getEvents'),
    path('createevent/<int:university_id>', views.createevent, name='createevent'),
]