from django.urls import path

from . import views

app_name = 'universities'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:university_id>', views.detail, name='detail'),
    path('createUniversity/', views.createUniversity, name='createUniversity'),
    path('submitcreateUniversity/', views.submitcreateUniversity, name='submitcreateUniversity'),
    path('searchUniversity/', views.searchUniversity, name='searchUniversity'),
    path('search/<str:searchText>', views.searchUniversityPage, name='searchUniversityPage')
]