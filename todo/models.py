from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """Task model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    title = models.CharField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username}: {self.title}'

    class Meta:
        ordering = ['-created_at']