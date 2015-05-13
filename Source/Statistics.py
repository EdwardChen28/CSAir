__author__ = 'Edward'
import sys


class Statistics:

    def __init__(self, airport_list):
        self.airport_list = airport_list

    # get the longest single flight
    def get_longest_flight(self):
        distance = 0
        for airport in self.airport_list:
            routes = self.airport_list[airport].routes

            for route in routes:
                if routes[route] > distance:
                    departure = self.airport_list[airport].name
                    destination = self.airport_list[route].name
                    distance = routes[route]
        return "Longest flight is from " + departure + " to " + destination + " : " + str(distance) + " km"

    # get the shortest single flight
    def get_shortest_flight(self):
        distance = sys.maxsize
        for airport in self.airport_list:
            routes = self.airport_list[airport].routes
            for route in routes:
                if routes[route] < distance:
                    departure = self.airport_list[airport].name
                    destination = self.airport_list[route].name
                    distance = routes[route]
        return "Shortest flight is from " + departure + " to " + destination + " : " + str(distance) + " km"

    # average distance of all flights
    def get_average_distance(self):
        total = 0
        route_count = 0
        for airport in self.airport_list:
            routes = self.airport_list[airport].routes
            for route in routes:
                total += routes[route]
                route_count += 1
        return int(total/route_count)

    # biggest city
    def get_biggest_city(self):
        population = 0
        for airport in self.airport_list:
            if self.airport_list[airport].population > population:
                population = self.airport_list[airport].population
                city = self.airport_list[airport].name
        return city

    # smallest city
    def get_smallest_city(self):
        population = sys.maxsize
        for airport in self.airport_list:
            if self.airport_list[airport].population < population:
                population = self.airport_list[airport].population
                city = self.airport_list[airport].name
        return city

    # average size by population
    def get_average_population(self):
        population = 0
        city_count = 0
        for airport in self.airport_list:
            population += self.airport_list[airport].population
            city_count += 1
        return int(population/city_count)

    # list of continents and city (continent : city)
    def get_continents(self):
        continent_list = []
        for airport in self.airport_list:
            continent_list.append(self.airport_list[airport].continent + " : " + self.airport_list[airport].name)
        return continent_list

    # get hub city
    def get_hub_cities(self):
        max_connection = 0
        # find the max connection
        for airport in self.airport_list:
            connection = 0
            connection += len(self.airport_list[airport].routes)
            for searchCity in self.airport_list:
                if searchCity != airport:
                    routes = self.airport_list[searchCity].routes
                    for route in routes:
                        if route == airport:
                            connection += 1
            if connection > max_connection:
                max_connection = connection
        string = self.hub_city(max_connection)
        return string[:-2]

    def hub_city(self, connection_num):
        string = ''
        for airport in self.airport_list:
            name = self.airport_list[airport].name
            connection = 0
            connection += len(self.airport_list[airport].routes)
            for searchCity in self.airport_list:
                if searchCity != airport:
                    routes = self.airport_list[searchCity].routes
                    for route in routes:
                        if route == airport:
                            connection += 1
            if connection == connection_num:
                string += name + ", "
        return string