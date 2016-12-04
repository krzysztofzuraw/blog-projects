import uuid

from django.db import models


def unique_file_path(instance, filename):
    new_file_name = uuid.uuid4()
    return '{}'.format(str(new_file_name))

class AudioFile(models.Model):
    name = models.CharField(max_length=100, blank=True)
    mp3_file = models.FileField(upload_to=unique_file_path)
    ogg_file = models.FileField(blank=True, upload_to=unique_file_path)
    wav_file = models.FileField(blank=True, upload_to=unique_file_path)
    ac3_file = models.FileField(blank=True, upload_to=unique_file_path)
    was_processed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
