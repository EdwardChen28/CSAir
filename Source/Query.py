__author__ = 'Edward'


class Query:

    def __init__(self, airport_list, city_to_code):
        self.airportList = airport_list
        self.cityToCode = city_to_code

    # get info about a route
    # given a list of cities, to return total distance, cost of fly, and time
    def get_route_info(self, city_list):
        cost = 0.35
        price = 0
        total_distance = 0
        distance_list = []
        for i in range(len(city_list)-1):
            code = self.cityToCode[city_list[i].lower()]
            code2 = self.cityToCode[city_list[i+1].lower()]
            current_distance = self.airportList[code].routes[code2]
            distance_list.append(current_distance)
            total_distance += current_distance
            price += current_distance*cost
            cost -= 0.05
        # for those greater than 400 km: 200 = 1/2 * 750 * time
        # for those greater than 400 km: 200 = 750*time - 1/2*750*time
        # the time spend on accelerating and decelerating to 750kph is the same
        acceleration_time = 32  # in minutes
        # since the acceleration is increasing uniformly. a = 750/(32/60) = 1406.25 constantly
        # formula => distance = 1/2 * a * time
        acceleration = 1406.25
        time = self.find_time(city_list, distance_list, acceleration_time, acceleration)
        return "total distance: " + str(total_distance) + "   " + "cost: " + str(price) + "   " + "time: " + str(time)

    def find_time(self, city_list, distance_list, acceleration_time, acc):

        time = 0  # in minutes
        # layover time
        for i in range(1, len(city_list)-1):
            code = self.cityToCode[city_list[i].lower()]
            route_number = len(self.airportList[code].routes)
            time += 120 - (route_number - 1)*10
        for i in distance_list:
            if i > 400:
                time += acceleration_time*2 + (i-400)/750*60
            else:
                half = float(i/2)
                time += half*2/acc * 60
        return time

    # get all the cities
    def get_cities(self):
        cities = []
        for city in self.airportList:
            cities.append(self.airportList[city].name)
        return cities

    # get city code from a city
    def get_city_code(self, city):
        return self.cityToCode[city.lower()]

    # get country
    def get_country(self, city):
        code = self.cityToCode[city.lower()]
        return self.airportList[code].country

    # get continent
    def get_continent(self, city):
        code = self.cityToCode[city.lower()]
        return self.airportList[code].continent

    # get timezone
    def get_timezone(self, city):
        code = self.cityToCode[city.lower()]
        return self.airportList[code].timezone

    # get latitude and longitude
    def get_coordinate(self, city):
        code = self.cityToCode[city.lower()]
        return self.airportList[code].coordinate

    # get population
    def get_population(self, city):
        code = self.cityToCode[city.lower()]
        return self.airportList[code].population

    # get region
    def get_region(self, city):
        code = self.cityToCode[city.lower()]
        return self.airportList[code].region

    # get routes and distance (city : distance)
    def get_route(self, city):
        code = self.cityToCode[city.lower()]
        routes = self.airportList[code].routes
        route_list = []
        for route in routes:
            destination = self.airportList[route].name
            distance = routes[route]
            route_list.append(city + " to " + destination +" : "+str(distance))
        return route_list