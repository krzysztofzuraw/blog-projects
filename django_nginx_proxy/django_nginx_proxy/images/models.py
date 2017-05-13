from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=100)
    image_file = models.ImageField(blank=True)

    def __str__(self):
        return 'Image: {}'.format(self.title)
