from django.contrib import admin
from .models import Posts


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'is_recommend')
    list_filter = ('publish', 'author')
    search_fields = ('title', 'content')
    ordering = ['-publish', 'author']
    date_hierarchy = 'publish'


admin.site.register(Posts, PostsAdmin)
