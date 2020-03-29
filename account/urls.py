from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='user_logout'),
    path('register/', views.register, name='user_register')
]
