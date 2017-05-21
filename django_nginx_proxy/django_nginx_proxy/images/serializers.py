from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    image_link = serializers.SerializerMethodField('get_url')

    class Meta:
        model = Image
        fields = ('title', 'image_link')
        read_only_fields = ('image_link',)

    def get_url(self, obj):
        request = self.context['request']
        return reverse('api:download-image', kwargs={'image_id': obj.id}, request=request)
