from unittest import TestCase

from Source.Parse import Parse
from Source.Statistics import Statistics

__author__ = 'Edward'


class TestStatistics(TestCase):
    def setUp(self):
        self.data = Parse("../UI/data.json")
        self.stat = Statistics(self.data.airportList)

    def test_get_longest_flight(self):
        string = "Longest flight is from Sydney to Los Angeles : 12051 km"
        self.assertEqual(self.stat.get_longest_flight(), string)

    def test_get_shortest_flight(self):
        string = "Shortest flight is from Washington to New York : 334 km"
        self.assertEqual(self.stat.get_shortest_flight(), string)

    def test_get_average_distance(self):
        self.assertEqual(self.stat.get_average_distance(), 2300)

    def test_get_biggest_city(self):
        self.assertEqual(self.stat.get_biggest_city(), "Tokyo")

    def test_get_smallest_city(self):
        self.assertEqual(self.stat.get_smallest_city(), "Essen")

    def test_get_average_population(self):
        self.assertEqual(self.stat.get_average_population(), 11796143)

    def test_get_continents(self):
        self.assertEqual(len(self.stat.get_continents()), 48)

    def test_get_hub_city(self):
        self.assertEqual(self.stat.get_hub_cities(), 'Istanbul, Hong Kong' or 'Hong Kong, Istanbul')