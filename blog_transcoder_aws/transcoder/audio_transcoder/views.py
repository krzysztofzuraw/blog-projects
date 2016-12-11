from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import AudioFileFrom
from .models import AudioFile
from aws_transcoder.transcoder import transcoder


class UploadAudioFileView(FormView):
    template_name = 'upload.html'
    form_class = AudioFileFrom

    def form_valid(self, form):
        audio_file = AudioFile(
            name=self.get_form_kwargs().get('data')['name'],
            mp3_file=self.get_form_kwargs().get('files')['mp3_file']
        )
        audio_file.save()
        wav_filename, flac_filename, mp4_filename = transcoder.start_transcode(
            filename=audio_file.mp3_file.name
        )
        audio_file.mp4_file = mp4_filename
        audio_file.flac_file = flac_filename
        audio_file.wav_file = wav_filename
        audio_file.save()
        return HttpResponseRedirect(
            reverse('audio:detail', kwargs={'pk': audio_file.pk})
        )

    def get_success_url(self):
        return reverse('home')


class AudioFileDetailView(DetailView):
    template_name = 'audiofile_detail.html'
    model = AudioFile
