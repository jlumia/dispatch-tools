from django.contrib.gis.db import models

class Airport(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=255)
    geom = models.PointField(srid=4326)

    class Meta:
        db_table = 'airports'
        verbose_name = 'Airport'
        verbose_name_plural = 'Airports'
