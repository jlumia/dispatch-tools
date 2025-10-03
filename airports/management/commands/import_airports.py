import requests
from django.contrib.gis.geos import Point
from django.core.management import BaseCommand

from airports.models import Airport


class Command(BaseCommand):

    def handle(self, *args, **options):
        response = requests.get('https://aviationweather.gov/api/data/airport?ids=kord&format=json').json()

        for i in response:
            a = Airport.objects.create(name=i['name'], abbreviation=i['icaoId'], geom=Point(i['lat'], i['lon']))
            print(a)

        # Airport.objects.create()
        #
        # print(response)

        print(f'Finished')
