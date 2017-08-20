import requests

from django.utils.functional import cached_property

from django.conf import settings

URL = "https://api.themoviedb.org/3/search/movie"


class ExternalMovie(object):

    session = requests.Session()

    def __init__(self, title):
        self._payload = {'api_key': settings.TMDB_API_KEY, 'query': title}

    @cached_property
    def description(self):
        response = self.session.get(URL, data=self._payload)
        response.raise_for_status()
        return response.json()['results'][0]['overview']
