from django.db import models


class Film(models.Model):
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    title = models.CharField(max_length=100)
    year = models.DateField()
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    actors = models.ManyToManyField('actors.Actor')

    def __str__(self):
        return f'Film: {self.title}'
