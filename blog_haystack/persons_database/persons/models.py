from django.db import models

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)

    def __str__(self):
        return '{first_name} {last_name}'.format(first_name=self.first_name, last_name=self.last_name)
