from __future__ import unicode_literals
from django.db import models
# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class Voivodeship(models.Model):
    iip_przest = models.CharField(max_length=255)
    iip_identy = models.CharField(max_length=255)
    iip_wersja = models.CharField(max_length=255)
    jpt_sjr_ko = models.CharField(max_length=255)
    jpt_kod_je = models.CharField(max_length=255)
    jpt_nazwa_field = models.CharField(max_length=255)
    jpt_nazw01 = models.CharField(max_length=255)
    jpt_organ_field = models.CharField(max_length=255)
    jpt_orga01 = models.CharField(max_length=255)
    jpt_jor_id = models.FloatField()
    wazny_od = models.DateField(null=True, blank=True)
    wazny_do = models.DateField(null=True, blank=True)
    jpt_wazna_field = models.CharField(max_length=255)
    wersja_od = models.DateField(null=True, blank=True)
    wersja_do = models.DateField(null=True, blank=True)
    jpt_powier = models.FloatField()
    jpt_kj_iip = models.CharField(max_length=255)
    jpt_kj_i01 = models.CharField(max_length=255)
    jpt_kj_i02 = models.CharField(max_length=255)
    jpt_kod_01 = models.CharField(max_length=255)
    id_bufora_field = models.FloatField()
    id_bufor01 = models.FloatField()
    id_technic = models.FloatField()
    jpt_opis = models.CharField(max_length=255)
    jpt_sps_ko = models.CharField(max_length=255)
    gra_ids = models.CharField(max_length=255)
    status_obi = models.CharField(max_length=255)
    opis_bledu = models.CharField(max_length=255)
    typ_bledu = models.CharField(max_length=255)
    geom = models.MultiPolygonField(srid=2180)

    def __str__(self):
        return '{}'.format(self.jpt_nazwa_field)

    def __unicode__(self):
        return '{}'.format(self.jpt_nazwa_field)

# Auto-generated `LayerMapping` dictionary for Voivodeship model
voivodeship_mapping = {
    'iip_przest' : 'iip_przest',
    'iip_identy' : 'iip_identy',
    'iip_wersja' : 'iip_wersja',
    'jpt_sjr_ko' : 'jpt_sjr_ko',
    'jpt_kod_je' : 'jpt_kod_je',
    'jpt_nazwa_field' : 'jpt_nazwa_',
    'jpt_nazw01' : 'jpt_nazw01',
    'jpt_organ_field' : 'jpt_organ_',
    'jpt_orga01' : 'jpt_orga01',
    'jpt_jor_id' : 'jpt_jor_id',
    'wazny_od' : 'wazny_od',
    'wazny_do' : 'wazny_do',
    'jpt_wazna_field' : 'jpt_wazna_',
    'wersja_od' : 'wersja_od',
    'wersja_do' : 'wersja_do',
    'jpt_powier' : 'jpt_powier',
    'jpt_kj_iip' : 'jpt_kj_iip',
    'jpt_kj_i01' : 'jpt_kj_i01',
    'jpt_kj_i02' : 'jpt_kj_i02',
    'jpt_kod_01' : 'jpt_kod_01',
    'id_bufora_field' : 'id_bufora_',
    'id_bufor01' : 'id_bufor01',
    'id_technic' : 'id_technic',
    'jpt_opis' : 'jpt_opis',
    'jpt_sps_ko' : 'jpt_sps_ko',
    'gra_ids' : 'gra_ids',
    'status_obi' : 'status_obi',
    'opis_bledu' : 'opis_bledu',
    'typ_bledu' : 'typ_bledu',
    'geom' : 'MULTIPOLYGON',
}

class Point(models.Model):
    name = models.CharField(max_length=200)
    geom = models.PointField('longitude/latitude', blank=True, null=True)
    objects = models.GeoManager()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
