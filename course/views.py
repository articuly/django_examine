from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Course
from .forms import CourseCreateForm
from braces.views import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse


class CourseAllView(ListView):
    model = Course
    template_name = 'course/home.html'
    context_object_name = 'courses'


class UserMixin:  # 筛选用户的类
    def get_queryset(self):
        qs = super(UserMixin, self).get_queryset()
        return qs.filter(user=self.request.user)


class UserCourseMixin(UserMixin, LoginRequiredMixin):
    model = Course
    login_url = '/account/login/'


class CourseListView(UserCourseMixin, ListView):
    template_name = 'course/course_list.html'
    context_object_name = 'courses'


class CourseUpdateView(UserCourseMixin, UpdateView):
    fields = ['title', 'intro', 'video', 'attach']
    template_name = 'course/course_create.html'
    success_url = '/course/list/'


class CourseCreateView(UserCourseMixin, CreateView):
    fields = ['title', 'intro', 'video', 'attach']
    template_name = 'course/course_create.html'

    def post(self, request, *args, **kwargs):
        form = CourseCreateForm(request.POST, request.FILES)
        if form.is_valid():
            new_course = form.save(commit=False)
            new_course.user = self.request.user
            new_course.save()
            return redirect('course:course_list')
        return self.render_to_response({'form': form})


class CourseDetailView(UserCourseMixin, DetailView):
    template_name = 'course/course_detail.html'


class CourseDeleteView(UserCourseMixin, DeleteView):
    success_url = reverse_lazy('course:course_list')

    def dispatch(self, *args, **kwargs):
        r = DeleteView.dispatch(self, *args, **kwargs)
        if self.request.is_ajax():
            return JsonResponse({'result': 'OK'})
        else:
            return r
