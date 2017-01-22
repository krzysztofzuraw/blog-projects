from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^audio/', include('audio_transcoder.urls', namespace='audio')),
    url(
        r'^messages/',
        include(
            'transcode_messages.urls',
            namespace='messages'
        )
    ),
]
