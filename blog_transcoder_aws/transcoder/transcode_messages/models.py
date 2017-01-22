from django.db import models


class Message(models.Model):
    text = models.CharField(max_length=250)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.text
