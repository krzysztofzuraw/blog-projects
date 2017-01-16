import json
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView, View
from django.http import (
    HttpResponseRedirect,
    HttpResponse,
    HttpResponseNotAllowed,
    HttpResponseForbidden
)
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.conf import settings


from .forms import AudioFileFrom
from .models import AudioFile
from .utlis import convert_sns_str_to_json
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


@csrf_exempt
def transcode_complete(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(request.method)
    if request.META['HTTP_X_AMZ_SNS_TOPIC_ARN'] != settings.SNS_TOPIC_ARN:
        return HttpResponseForbidden('Not vaild SNS topic ARN')
    json_body = json.loads(request.body.decode('utf-8'), object_hook=convert_sns_str_to_json)
    if json_body['Message']['state'] == 'COMPLETED':
        # do something
        pass
    return HttpResponse('OK')
