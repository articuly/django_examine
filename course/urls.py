from django.urls import path
from .views import CourseAllView, CourseListView, CourseDetailView, CourseCreateView

app_name = 'course'

urlpatterns = [
    path('', CourseAllView.as_view(), name='course_home'),
    path('list/', CourseListView.as_view(), name='course_list'),
    path('create/', CourseCreateView.as_view(), name='course_create'),
    path('detail/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
]
