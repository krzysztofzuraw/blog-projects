import os

from django.conf import settings

import boto3


class AudioTranscoder(object):

    def __init__(self, region_name='eu-west-1', pipeline_name='Audio Files'):
        self.region_name = region_name
        self.pipeline_name = pipeline_name
        self.transcoder = boto3.client('elastictranscoder', self.region_name)
        self.pipeline_id = self.get_pipeline()

    def get_pipeline(self):
        paginator = self.transcoder.get_paginator('list_pipelines')
        for page in paginator.paginate():
            for pipeline in page['Pipelines']:
                if pipeline['Name'] == self.pipeline_name:
                    return pipeline['Id']

    def start_transcode(self, filename):
        base_filename, _ = self.create_aws_filename(filename, '')
        wav_aws_filename, wav_filename = self.create_aws_filename(
            filename, extension='.wav'
        )
        flac_aws_filename, flac_filename = self.create_aws_filename(
            filename, extension='.flac'
        )
        mp4_aws_filename, mp4_filename = self.create_aws_filename(
            filename, extension='.mp4'
        )
        self.transcoder.create_job(
            PipelineId=self.pipeline_id,
            Input={
                'Key': base_filename,
                'FrameRate': 'auto',
                'Resolution': 'auto',
                'AspectRatio': 'auto',
                'Interlaced': 'auto',
                'Container': 'auto'
            },
            Outputs=[{
                'Key': wav_aws_filename,
                'PresetId': '1351620000001-300300'
                }, {
                'Key': flac_aws_filename,
                'PresetId': '1351620000001-300110'
                }, {
                'Key': mp4_aws_filename,
                'PresetId': '1351620000001-100110'
                }
            ]
        )
        return (wav_filename, flac_filename, mp4_filename)

    @staticmethod
    def create_aws_filename(filename, extension):
        aws_filename = os.path.join(
            settings.MEDIAFILES_LOCATION, filename + extension
        )
        return aws_filename, os.path.basename(aws_filename)


transcoder = AudioTranscoder()
