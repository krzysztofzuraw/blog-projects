from django.conf.urls import include, url

from rest_framework import routers

from .views import ImagesViewSet, download_image_view

router = routers.DefaultRouter()
router.register(r'images', ImagesViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^download/image/(?P<image_id>\d+)/$', download_image_view, name='download-image')
]
