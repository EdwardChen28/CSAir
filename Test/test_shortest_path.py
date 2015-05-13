from unittest import TestCase
from Source.Parse import Parse
from Source.ShortestPath import shortest_path
import sys
__author__ = 'Edward'


class Test_Shortest_path(TestCase):

    def setUp(self):
        self.data = Parse("../UI/data.json")

    def test_shortest_path(self):
        distance = shortest_path(self.data.airportList, self.data.cityToCode, "Madrid", "New York")
        self.assertEqual(distance, 5786)
        distance = shortest_path(self.data.airportList, self.data.cityToCode, "Lima", "Miami")
        self.assertEqual(distance, 4304)
        print(shortest_path(self.data.airportList, self.data.cityToCode, "Los Angeles", "Atlanta"))