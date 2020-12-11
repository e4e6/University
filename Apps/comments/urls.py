from django.urls import path

from . import views

app_name = 'comments'
urlpatterns = [
    path('', views.index, name='index'),
    path('createpost/', views.createpost, name='createpost'),
    path('deletepost/<int:post_id>', views.deletepost, name='deletepost'),
    path('editpost/', views.editpost, name='editpost'),
]