__author__ = 'Edward'
from Source.Airport import Airport


class Modification:

    def __init__(self, airports, city_code):
        self.airports = airports
        self.city_code = city_code

    def remove_city(self, city):
        code = self.city_code[city]
        self.airports.pop(code, 0)
        self.city_code.pop(city, 0)
        # TODO .....

    def remove_route(self, depart, destination):
        code_depart = self.city_code[depart.lower()]
        routes = self.airports[code_depart].routes
        for route in routes:
            if route == self.city_code[destination.lower()]:
                routes.pop(route, 0)
                return

    def add_city(self, code, city, country, continent, timezone, dict_obj, population, region):
        self.city_code[city.lower()] = code
        obj = Airport(code, city, country, continent, timezone, dict_obj, population, region)
        self.airports[code] = obj

    def add_route(self, depart, destination, distance):
        code = self.city_code[depart]
        code2 = self.city_code[destination]
        self.airports[code].routes[code2] = distance

    # return true if succeeded
    def edit_coordinate(self, city, coordinate):
        dict_obj = self.convert_to_dict(coordinate)
        if dict_obj == -1:
            return False
        self.airports[self.city_code[city.lower()]].coordinate = dict_obj
        return True

    def convert_to_dict(self, string):
        words = string.split(' ')
        if len(words) > 4:
            return -1
        try:
            first = int(words[1])
            second = int(words[3])
        except ValueError:
            return -1
        if len(words[0]) > 1 or len(words[2]) > 1:
            return -1
        coordinate = {words[0]: first, words[2]: second}
        return coordinate

    # change population of a city
    def edit_population(self, city, new_population):
        self.airports[self.city_code[city.lower()]].population = new_population

    # change region
    def edit_region(self, city, region):
        self.airports[self.city_code[city.lower()]].region = region

    # change city's country
    def edit_country(self, city, country):
        self.airports[self.city_code[city.lower()]].country = country

    # change timezone
    def edit_timezone(self, city, timezone):
        self.airports[self.city_code[city.lower()]].timezone = timezone

    # change continent
    def edit_continent(self, city, continent):
        self.airports[self.city_code[city.lower()]].continent = continent

    # change city code
    def edit_code(self, city, code):
        # update airport list and city to code dictionary structure
        old_code = self.city_code[city.lower()]
        self.airports[code] = self.airports[old_code]
        del self.airports[old_code]
        self.city_code[city.lower()] = code
        # change all the route to the new code
        for ap in self.airports:
            routes = self.airports[ap].routes
            for route in routes:
                if route == old_code:
                    routes[code] = routes[route]
                    del routes[route]