from .views import VerificationView
from django.contrib.auth.views import PasswordResetDoneView
from django.urls import path,include
from django.contrib.auth import views as auth_views

from . import views
from django.urls import reverse_lazy

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
    # path('password_change/', views.password_changeaa, name='password_changeaa'),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('change_password/', auth_views.PasswordChangeView.as_view(),{'post_change_redirect' : '/change_password_done/'}, name='change_password'),
    #path('change_password_done/', auth_views.PasswordChangeDoneView.as_view(),name='change_password_done')
    path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('users:password_change_done'),),
         name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    
    path('password_reset/',auth_views.PasswordResetView.as_view(email_template_name = 'users/password_reset_email.html',success_url=reverse_lazy('users:password_reset_done'),template_name='users/password_reset.html'),name='password_reset'),
    path('password_reset_send/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_send.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('users:password_reset_complete'),template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
    path('activate/<uidb64>/<token>',VerificationView.as_view(),name='activate'   )


]
