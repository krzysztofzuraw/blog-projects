from rest_framework import serializers

from .models import Actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('first_name', 'last_name', 'age', 'rating')
