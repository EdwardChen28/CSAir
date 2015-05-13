from unittest import TestCase

from Source.Parse import Parse
from Source.Query import Query

__author__ = 'Edward'


class TestQuery(TestCase):
    def setUp(self):
        self.data = Parse("../UI/data.json")
        self.query = Query(self.data.airportList, self.data.cityToCode)

    def test_get_cities(self):
        self.assertEqual(len(self.query.get_cities()), 48)

    def test_get_city_code(self):
        self.assertEqual(self.query.get_city_code("Paris"), "PAR")

    def test_get_country(self):
        self.assertEqual(self.query.get_country("Paris"), "FR")

    def test_get_continent(self):
        self.assertEqual(self.query.get_continent("London"), "Europe")

    def test_get_timezone(self):
        self.assertEqual(self.query.get_timezone("London"), 0)

    def test_get_coordinate(self):
        self.assertEqual(self.query.get_coordinate("Cairo"), {"N": 30, "E": 31})

    def test_get_population(self):
        self.assertEqual(self.query.get_population("Cairo"), 15200000)

    def test_get_region(self):
        self.assertEqual(self.query.get_region("Cairo"), 2)

    def test_get_route(self):
        self.assertEqual(len(self.query.get_route("Paris")), 2)

    def test_get_route_info(self):
        info = self.query.get_route_info(['Lima', 'Bogota', "Miami"])
        # print(info)
        self.assertEqual(info, 'total distance: 4304   cost: 1385.15   time: 508.32')
        info2 = self.query.get_route_info(["Madrid", "New York"])
        # print(info2)
        self.assertEqual(info2, 'total distance: 5786   cost: 2025.1   time: 494.88')