from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^upload/$',
        view=views.UploadAudioFileView.as_view(),
        name='upload'
    ),
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=views.AudioFileDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^transcode-complete/$',
        view=views.transcode_complete,
        name='transcode-complete'
    )
]
