from django.http import HttpResponse
from rest_framework import viewsets

from .models import Image
from .serializers import ImageSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


def download_image_view(request, image_id):
    image = Image.objects.get(id=image_id)
    response = HttpResponse()
    response['X-Accel-Redirect'] = image.image_file.url
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(image.image_file.name)
    return response
