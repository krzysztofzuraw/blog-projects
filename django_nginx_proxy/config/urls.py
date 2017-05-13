from django.conf import settings
from django.conf.urls import url, include
from django.views.static import serve
from django.contrib import admin

urlpatterns = [
    url(r'^', include('django_nginx_proxy.images.urls', namespace='api')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
            url(r'^media/(?P<path>.*)$', serve, {
                'document_root': settings.MEDIA_ROOT,
            }),
        ]
