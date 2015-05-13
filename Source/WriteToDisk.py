__author__ = 'Edward'
import json


def write_to_disk(airports):
    metro_list = []
    routes_list = []
    data_source = ["http://www.gcmap.com/",
                   "http://www.theodora.com/country_digraphs.html",
                   "http://www.citypopulation.de/world/Agglomerations.html",
                   "http://www.mongabay.com/cities_urban_01.htm",
                   "http://en.wikipedia.org/wiki/Urban_agglomeration",
                   "http://www.worldtimezone.com/standard.html"]

    # create metro part
    for airport in airports:
        obj = airports[airport]
        temp = {
            "code": obj.code,
            "name": obj.name,
            "country": obj.country,
            "continent": obj.continent,
            "timezone": obj.timezone,
            "coordinates": obj.coordinate,
            "population": obj.population,
            "region": obj.region
        }
        metro_list.append(temp)

    # create route parts
    for airport in airports:
        obj = airports[airport]
        routes = obj.routes
        for route in routes:
            temp = {
                "ports": [airport, route],
                "distance": routes[route]
            }
            routes_list.append(temp)

    whole_list = json.dumps({"data sources": data_source, "metros": metro_list, "routes": routes_list})
    json_file = open("updated.json", "wb+")
    json_file.write(bytes(whole_list, 'UTF-8'))
    json_file.close()