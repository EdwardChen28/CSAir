__author__ = 'Edward'
import webbrowser
from Source.Parse import Parse
from Source.Query import Query
from Source.Statistics import Statistics
from Source.WriteToDisk import write_to_disk

def main():
    print("Welcome to CS Airline")
    data = Parse("updated.json")
    #data = Parse("data.json")
    #data.parse_data("cmi_hub.json")
    while True:
        main_menu()
        while True:
            try:
                user_input = int(input())
                break
            except ValueError:
                print("That was not a valid number. Try Again!")
        if user_input == 1:
            city_info(data.airportList, data.cityToCode)
        elif user_input == 2:
            statistics(data.airportList)
        elif user_input == 3:
            visualizing(data.airportList)
        elif user_input == 0:
            write_to_disk(data.airportList)
            return


# visualize in map
def visualizing(airport_list):
    url = "http://www.gcmap.com/mapui?P="
    string = ""
    for i in airport_list:
        routes = airport_list[i].routes
        for j in routes:
            string += i + "-" + j + ",+"
    webbrowser.open(url+string[:-2])


def statistics(airport_list):
    stat = Statistics(airport_list)
    while True:
        stat_info_selection()
        while True:
            try:
                selection = int(input())
                break
            except ValueError:
                print("That was not a valid number. Try Again!")

        if selection == 1:
            print(stat.get_longest_flight())
        elif selection == 2:
            print(stat.get_shortest_flight())
        elif selection == 3:
            print(stat.get_average_distance())
        elif selection == 4:
            print(stat.get_biggest_city())
        elif selection == 5:
            print(stat.get_smallest_city())
        elif selection == 6:
            print(stat.get_average_population())
        elif selection == 7:
            print(stat.get_continents())
        elif selection == 8:
            print(stat.get_hub_cities())
        else:
            break


def stat_info_selection():
    print("press 1 for the longest single flight")
    print("press 2 for the shortest single flight")
    print("press 3 for the average distance of all the flights")
    print("press 4 for the biggest city airport location in population")
    print("press 5 for the smallest city airport location in population")
    print("press 6 for average population of all cities served by CS Airline")
    print("press 7 for the list of the continents served by CS Airline and the cities are in them")
    print("press 8 for the hub city ")


def city_info(airport_list, city_code):
    query = Query(airport_list, city_code)
    # handling city input exception
    while True:
        print("please enter the city name:")
        city = input().lower()
        if query.cityToCode[city] != -1:
            break
        print("invalid key!")

    while True:
        city_info_selection()
        # handling input exception
        while True:
            try:
                selection = int(input())
                break
            except ValueError:
                print("That was not a valid number. Try Again!")
        if selection == 1:
            print(query.get_city_code(city))
        elif selection == 2:
            print(query.get_country(city))
        elif selection == 3:
            print(query.get_continent(city))
        elif selection == 4:
            print(query.get_timezone(city))
        elif selection == 5:
            print(query.get_coordinate(city))
        elif selection == 6:
            print(query.get_population(city))
        elif selection == 7:
            print(query.get_region(city))
        elif selection == 8:
            print(query.get_route(city))
        else:
            break


def city_info_selection():
    print("press 1 for the city code")
    print("press 2 for the country of city ")
    print("press 3 for the continent the city locates")
    print("press 4 for the time zone of the city")
    print("press 5 for the latitude and longitude of the city")
    print("press 6 for the city population")
    print("press 7 for the region of the city")
    print("press 8 for all the non-stop flights form the city")


def main_menu():
    print("Please select your services")
    print("press 1 to get city information")
    print("press 2 to get CS Airline statistic information")
    print("press 3 to get a map")
    print("press 0 to leave")


if __name__ == '__main__':
    main()

