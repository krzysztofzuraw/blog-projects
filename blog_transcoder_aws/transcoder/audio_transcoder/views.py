from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import AudioFileFrom
from .models import AudioFile

from taskapp.tasks import transcode_mp3

class UploadAudioFileView(FormView):
    template_name = 'upload.html'
    form_class = AudioFileFrom

    def form_valid(self, form):
        audio_file = AudioFile(
            name=self.get_form_kwargs().get('data')['name'],
            mp3_file=self.get_form_kwargs().get('files')['mp3_file']
        )
        audio_file.save()
        #transcode_mp3.delay(audio_file.id)
        return HttpResponseRedirect(reverse('audio:detail', kwargs={'pk': audio_file.pk}))

    def get_success_url(self):
        return reverse('home')


class AudioFileDetailView(DetailView):
    template_name = 'audiofile_detail.html'
    model = AudioFile
