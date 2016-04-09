import uuid

from django.db import models


def md5_directory_path(instance, filename):
    new_file_name = uuid.uuid4()
    return str(new_file_name)

class AudioFile(models.Model):
    name = models.CharField(max_length=100, blank=True)
    mp3_file = models.FileField(upload_to=md5_directory_path)
    ogg_file = models.FileField(blank=True, upload_to=md5_directory_path)
    wav_file = models.FileField(blank=True, upload_to=md5_directory_path)
    ac3_file = models.FileField(blank=True, upload_to=md5_directory_path)
    was_processed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
