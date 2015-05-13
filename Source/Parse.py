__author__ = 'Edward'
import json
from collections import defaultdict
from Source.Airport import Airport


class Parse:

    def __init__(self, filename):
        self.airportList = {}  # mapping city code to its airport object
        self.cityToCode = {}  # mapping city name to city code, very useful in query
        self.parse_data(filename)
        self.airportList = defaultdict(lambda: -1, self.airportList)
        self.cityToCode = defaultdict(lambda: -1, self.cityToCode)

    def parse_data(self, filename):
        file = open(filename)
        data = json.load(file)

        for airport in data["metros"]:
            code = airport['code']
            name = airport['name']
            country = airport['country']
            continent = airport['continent']
            timezone = airport['timezone']
            coordinates = airport['coordinates']
            population = airport['population']
            region = airport['region']
            obj = Airport(code, name, country, continent, timezone, coordinates, population, region)
            self.airportList[obj.code] = obj
            self.cityToCode[obj.name.lower()] = obj.code

        for route in data['routes']:
            depart = route['ports'][0]
            destination = route['ports'][1]
            distance = route['distance']
            self.airportList[depart].routes[destination] = distance

    # read another file and store the data to current data structure
