from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'create_time')
    list_filter = ('create_time',)
    search_fields = ('title', 'intro', 'content')
    ordering = ['-create_time', 'user']
    date_hierarchy = 'create_time'


admin.site.register(Course, CourseAdmin)
