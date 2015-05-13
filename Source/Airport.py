__author__ = 'Edward'
from collections import defaultdict


class Airport:

    def __init__(self, code, name, country, continent, timezone, coordinates, population, region):
        self.code = code
        self.name = name
        self.country = country
        self.continent = continent
        self.timezone = timezone
        self.coordinate = coordinates
        self.population = population
        self.region = region
        # dictionary: map the destination with distance
        self.routes = {}
        self.routes = defaultdict(lambda: -1, self.routes)