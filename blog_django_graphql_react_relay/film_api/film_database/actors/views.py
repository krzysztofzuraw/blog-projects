from rest_framework import viewsets

from .models import Actor
from .serializers import ActorSerializer


class ActorsViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
