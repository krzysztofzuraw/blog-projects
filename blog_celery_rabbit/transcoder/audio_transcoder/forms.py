from django.forms import ModelForm
from .models import AudioFile


class AudioFileFrom(ModelForm):

    class Meta:
        model = AudioFile
        fields = ['name', 'mp3_file']
