from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('post/', views.blog_post, name='blog_post'),
]
