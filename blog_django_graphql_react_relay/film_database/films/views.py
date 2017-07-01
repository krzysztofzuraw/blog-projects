from rest_framework import viewsets

from .models import Film
from .serializers import FilmSerializer


class FilmsViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
