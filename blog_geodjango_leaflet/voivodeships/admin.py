from django.contrib.gis import admin
from .models import Voivodeship, Point

admin.site.register(Voivodeship, admin.OSMGeoAdmin)
admin.site.register(Point, admin.OSMGeoAdmin)
