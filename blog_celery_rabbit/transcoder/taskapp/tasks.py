from __future__ import absolute_import
import os
import os.path
import subprocess

from celery.signals import task_postrun

from taskapp.celery import app
from audio_transcoder.models import AudioFile
from celery.utils.log import get_task_logger

import config.settings as settings


logger = get_task_logger(__name__)


@app.task
def transcode_mp3(mp3_id):
    audio_file = AudioFile.objects.get(id=mp3_id)
    input_file_path = audio_file.mp3_file.path
    filename = os.path.basename(input_file_path)
    ogg_output_file_name = os.path.join('transcoded', '{}.ogg'.format(filename))
    ogg_output_file_path = os.path.join(settings.MEDIA_ROOT, ogg_output_file_name)

    ac3_output_file_name = os.path.join('transcoded', '{}.ac3'.format(filename))
    ac3_output_file_path = os.path.join(settings.MEDIA_ROOT, ac3_output_file_name)

    wav_output_file_name = os.path.join('transcoded', '{}.wav'.format(filename))
    wav_output_file_path = os.path.join(settings.MEDIA_ROOT, wav_output_file_name)

    logger.debug(
        'Created output files: %s, %s, %s.',
        ogg_output_file_path,
        ac3_output_file_path,
        wav_output_file_path
    )

    if not os.path.isdir(os.path.dirname(ogg_output_file_path)):
        logger.debug('Making directory %s.', os.path.dirname(ogg_output_file_path))
        os.makedirs(os.path.dirname(ogg_output_file_path))

    logger.info('Started transcoding.')
    subprocess.call([
            settings.FFMPEG_PATH,
            '-i',
            input_file_path,
            ogg_output_file_path,
            ac3_output_file_path,
            wav_output_file_path
        ]
    )
    logger.info('End of transcoding.')

    audio_file.ogg_file = ogg_output_file_name
    audio_file.ac3_file = ac3_output_file_name
    audio_file.wav_file = wav_output_file_name
    audio_file.save()

@task_postrun.connect
def task_executed_handler(sender=None, body=None, **kwargs):
    audio_file = AudioFile.objects.get(id=kwargs['args'][0])
    audio_file.was_processed = True
    audio_file.save()
    logger.debug('AudioFile was processed.')
