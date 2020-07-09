from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'account'

urlpatterns = [
    path('', views.home, name='home'),

    # register
    path('register/', views.register, name='register'),
    # login / logout urls
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),

    # change password urls
    path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy(
        'account:password_change_done'), template_name='account/password_change_form.html'), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='account/password_change_done.html'), name='password_change_done'),

    # change password with email urls
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset_form.html',
                                                                 email_template_name='account/password_reset_email.html',
                                                                 subject_template_name=
                                                                 'account/password_reset_email.txt'),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='account/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='account/password_reset_complete.html'), name='password_reset_complete')

]
