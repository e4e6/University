from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profileEdit/', views.profileEdit, name='profileEdit'),
    path('universities/', views.universityList, name='universityList'),
    path('events/', views.eventList, name='eventList'),
]