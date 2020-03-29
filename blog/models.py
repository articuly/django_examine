from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Posts(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    is_recommend = models.BooleanField(default=False)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
