from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Point, Voivodeship
from django.views.generic import TemplateView
from django.core.cache import cache


def points_view(request):
    points_as_geojson = serialize('geojson', Point.objects.all())
    return HttpResponse(points_as_geojson, content_type='json')


def voivodeships_view(request):
    redis_key = 'voivodeships'
    voivodeships = cache.get(redis_key)
    if not voivodeships:
        voivodeships = serialize('geojson', Voivodeship.objects.all())
        cache.set(redis_key, voivodeships)
    return HttpResponse(voivodeships, content_type='json')


class MainPageView(TemplateView):
    template_name = 'voivodeships/index.html'
