# appmakales/urls.py
from django.urls import path
#from .views import HomePageView
from . import views
from os import name
from django.urls import path
from .views import (MakaleListView, MakaleDetailView, MakaleCreateView ,
MakaleUpdateView,MakaleDeleteView,)


# app_name = 'appmakales'
# urlpatterns = [
#     path('', views.makale_home, name='makale_home'),
#     path('create_makale/', views.create_makale, name='create_makale'),
#     path('delete_makale/<int:post_id>', views.delete_makale, name='delete_makale'),
#     path('edit_makale/', views.edit_makale, name='edit_makale'),
    
# ]
app_name = 'appmakales'
urlpatterns = [
path('makale/<int:pk>/delete/', MakaleDeleteView.as_view(), name='makale_delete'),
path('makale/new/', MakaleCreateView.as_view(), name='makale_new'),
path('makale/', MakaleListView.as_view(), name='makale_home'),
path('makale/<int:pk>/', MakaleDetailView.as_view(), name= 'makale_detail'),
path('makale/<int:pk>/edit/',MakaleUpdateView.as_view(), name='makale_edit'),
]