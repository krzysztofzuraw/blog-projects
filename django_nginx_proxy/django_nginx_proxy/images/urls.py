from django.conf.urls import include, url

from rest_framework import routers

from .views import ImagesViewSet

router = routers.DefaultRouter()
router.register(r'images', ImagesViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
]
