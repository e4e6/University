from django.urls import path

from . import views

app_name = 'universities'
urlpatterns = [
    path('', views.index, name='index'),
]