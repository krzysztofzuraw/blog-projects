from rest_framework import viewsets

from .models import Image
from .serializers import ImageSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
