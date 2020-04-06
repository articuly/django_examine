from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    return 'course/user_{0}/{1}'.format(instance.user.username, filename)


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses_user')
    title = models.CharField(max_length=128)
    intro = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)
    video = models.FileField(blank=True, upload_to=user_directory_path)
    attach = models.FileField(blank=True, upload_to=user_directory_path)

    class Meta:
        ordering = ('-create_time',)

    def __str__(self):
        return self.title
