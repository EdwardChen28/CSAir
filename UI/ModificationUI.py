__author__ = 'Edward'

from Source.Parse import Parse
from Source.WriteToDisk import write_to_disk
from Source.Modification import Modification


def main():
    print("Welcome to data modification interface")
    data = Parse("data.json")
    airports = data.airportList
    city_code = data.cityToCode
    modify = Modification(airports, city_code)
    while True:
        main_menu()
        while True:
            try:
                selection = int(input())
                break
            except ValueError:
                print("That was not a valid number. Try Again!")
        if selection == 1:
            city_removal_page(modify)
        elif selection == 2:
            route_removal_page(modify)
        elif selection == 3:
            city_add_page(modify)
        elif selection == 4:
            route_add_page(modify)
        elif selection == 5:
            city_edit_page(modify)
        elif selection == 0:
            print("Bye!!")
            break
    # saving the updated data into disk (or to a new file in this case)
    write_to_disk(airports)


def city_edit_page(modify):
    print("Please follow the instruction to edit an existing city")
    while True:
        print("Please enter the city name")
        city = input()
        if modify.city_code[city.lower()] != -1:
            break
        print("Not a valid name or the name is not exist in the database")

    while True:
        edit_city_menu()
        while True:
            try:
                selection = input()
                if selection.lower == 'b':
                    return
                selection = int(selection)
            except ValueError:
                print("Please enter a number to proceed or press b to leave ")
    if selection == 1:
        edit_code(modify, city)
    elif selection == 2:
        edit_country(modify, city)
    elif selection == 3:
        edit_continent(modify, city)
    elif selection == 4:
        edit_timezone(modify, city)
    elif selection == 5:
        edit_coordinate(modify, city)
    elif selection == 6:
        edit_population(modify, city)
    elif selection == 7:
        edit_region(modify, city)
    elif selection == 0:
        return


def edit_coordinate(modify,  city):
    while True:
        print("Please enter the coordinate of the city in the format as")
        print(" N 12 W 13   with space between each character")
        print("or press letter b to exit")
        coordinate = input()
        if coordinate.lower() == 'b':
            return
        dict_obj = modify.edit_coordinate(city, coordinate)
        if dict_obj:
            break
        print("That was not a valid coordinate format. Try Again!")


def edit_population(modify,  city):
    while True:
        print("Please enter the new population for the city")
        try:
            new_population = int(input())
        except ValueError:
            print("please enter a valid number")
        if new_population >= 0:
            break
        print("population can not be negative")

    modify.edit_population(city, new_population)


def edit_region(modify, city):
    while True:
        print("Please enter the new region number for the city")
        try:
            new_region = int(input())
        except ValueError:
            print("please enter a valid number")
        if new_region > 0:
            break
        print("population can not be negative")

    modify.edit_region(city, new_region)


def edit_country(modify, city):
    print("Please enter the new country for the city")
    new_country = input()
    modify.edit_country(city, new_country)


def edit_timezone(modify, city):
    print("Please enter the new timezone for the city")
    new_timezone = input()
    modify.edit_timezone(city, new_timezone)


def edit_continent(modify, city):
    print("Please enter the new continent for the city")
    new_continent = input()
    modify.edit_coordinate(city, new_continent)


def edit_code(modify, city):
    print("Please enter the new code for the city")
    new_code = input()
    modify.edit_code(city,new_code)


def edit_city_menu():
    print("Press 1 to edit the code ")
    print("Press 2 to edit the country")
    print("Press 3 to edit continent")
    print("Press 4 to edit timezone")
    print("press 5 to edit coordinate")
    print("press 6 to edit population")
    print("press 7 to edit the region")
    print("press 0 to leave")


def route_add_page(modify):
    print("You need to provide all the information we need in order to add a route successfully")
    print("You can press b to exit any time during the process")
    while True:
        print("Please enter the departure city")
        departure = input()
        if departure.lower() == 'b':
            return
        if modify.city_code[departure.lower()] != -1:
            break
        print("Not a valid city name or the city name does not exist. Try Again")

    while True:
        print("Please enter the destination city")
        destination = input()
        if destination.lower() == 'b':
            return
        if modify.city_code[destination.lower()] != -1:
            break
        print("Not a valid city name or the city name does not exist. Try Again")

    while True:
        print("Please enter the distance of this route")
        try:
            distance = input()
            if distance.lower() == 'b':
                return
        except ValueError:
            print("That was not a valid distance. Try Again")
    modify.add_route(departure, destination, distance)


def city_add_page(modify):
    print("Please note that you have to provide all the information we need in order to add a city")
    print("Press letter b to exit")

    print("please enter the city name")
    city = input()
    if city.lower() == 'b':
        return

    print("please enter the code of the city")
    code = input()
    if code.lower() == 'b':
        return

    print("Please enter the country that the city is located")
    country = input()
    if country.lower() == 'b':
        return

    print("Please enter the continent")
    continent = input()
    if continent.lower() == 'b':
        return

    while True:
        try:
            print("Please enter the timezone ")
            timezone = int(input())
        except ValueError:
            print("That was not a valid timezone. Try Again!")

    while True:
        print("Please enter the coordinate of the city in the format as")
        print(" N 12 W 13   with space between each character")
        coordinate = input()
        if modify.convert_to_dict(coordinate) != -1:
            coordinate = modify.convert_to_dict(coordinate)
            break
        print("That was not a valid coordinate format. Try Again!")

    while True:
        print("Please enter the city population")
        try:
            population = int(input())
        except ValueError:
            print("That was not a valid number. Try Again")
        if population > 0:
            break
        print("Population can not be negative")

    while True:
        print("Please enter the city region")
        try:
            region = int(input())
        except ValueError:
            print("That was not a valid region. Try Again!")
        if region >= 0:
            break

    modify.add_city(code, city, country, continent, timezone, coordinate, population, region)
    print("city was successfully added")
    return


# remove a route from the database
def route_removal_page(modify):
    print("To remove a route, you will need to provide the departure city name and destination")
    print("or press letter b to leave")
    while True:
        # get departure city
        while True:
            print("Please enter the name of the departure city")
            departure = input()
            if departure.lower() == 'b':
                return
            if modify.city_code[departure.lower()] != -1:
                break
            print("city name does not exist. Try Again!")
        # get destination city
        while True:
            print("Please enter the destination city name")
            destination = input()
            if destination.lower() == 'b':
                return
            if modify.city_code[destination.lower()] != -1:
                break
            print("city name does not exist. Try Again!")

        modify.remove_route(departure, destination)


# to remove a city from database
def city_removal_page(modify):
    print("Enter that city name to remove")
    print("or press letter b to previous page")
    while True:
        selection = input()
        if selection.lower() == 'b':
            return
        if modify.city_code[selection.lower()] != -1:
            break
        print("The city name you enter is not in database. Try Again!")
    modify.remove_city(selection)


def main_menu():
    print("Press 1 to remove a city. Note: all the information about the city will be removed also ")
    print("Press 2 to remove a route")
    print("press 3 to add a city")
    print("press 4 to add a route")
    print("press 5 to edit an existing city")
    print("press 0 to exit")

if __name__ == '__main__':
    main()


