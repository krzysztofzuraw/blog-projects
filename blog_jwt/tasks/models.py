from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=100)
    person = models.ForeignKey('auth.User', related_name='tasks')
    due_to = models.DateTimeField()

    def __str__(self):
        return 'Task with title: {}'.format(self.title)
