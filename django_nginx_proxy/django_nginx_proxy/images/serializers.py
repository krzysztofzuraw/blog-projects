from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('title', 'image_file')
