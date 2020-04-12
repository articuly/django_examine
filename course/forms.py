from django import forms
from .models import Course
from mdeditor.fields import MDTextFormField


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'intro', 'content', 'video', 'attach',)
