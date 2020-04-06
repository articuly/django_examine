from django.urls import path
from .views import CourseDeleteView, CourseAllView, CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView

app_name = 'course'

urlpatterns = [
    path('', CourseAllView.as_view(), name='course_home'),
    path('list/', CourseListView.as_view(), name='course_list'),
    path('create/', CourseCreateView.as_view(), name='course_create'),
    path('detail/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('delete/<int:pk>/', CourseDeleteView.as_view(), name='course_delete'),
    path('update/<int:pk>/', CourseUpdateView.as_view(), name='course_update'),
]
