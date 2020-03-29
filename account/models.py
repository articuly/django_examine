from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    phone = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=50, blank=True)
    job = models.CharField(max_length=100, blank=True)
    intro = models.TextField(blank=True)

    def __str__(self):
        return 'user: {}'.format(self.user.username)
