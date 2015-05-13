__author__ = 'Edward'
import sys


def shortest_path(airports, city_to_code, departure, destination):
    starting_point = city_to_code[departure.lower()]
    ending_point = city_to_code[destination.lower()]
    distance = {}
    visited = {}
    previous = {}
    for airport in airports:
        distance[airport] = sys.maxsize
        visited[airport] = False
    # set the starting point to 0 in distance
    distance[starting_point] = 0
    previous[starting_point] = None

    while find_min_distance(distance, visited) != ' ':
        current_node = find_min_distance(distance, visited)
        visited[current_node] = True
        routes = airports[current_node].routes
        for route in routes:
            if (distance[current_node] + routes[route]) < distance[route]:
                distance[route] = distance[current_node] + routes[route]
                previous[route] = current_node
    curr = ending_point
    print(curr)
    while curr != starting_point:
        print(previous[curr])
        curr = previous[curr]

    return distance[ending_point]


def find_min_distance(distance, visited):
    compare = sys.maxsize
    min_code = ' '
    for visit in visited:
        if not visited[visit]:
            if distance[visit] < compare:
                compare = distance[visit]
                min_code = visit
    return min_code