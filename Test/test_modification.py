from unittest import TestCase
from Source.Modification import Modification
from Source.Parse import Parse
__author__ = 'Edward'


class TestModification(TestCase):
    def setUp(self):
        self.data = Parse("../UI/data.json")
        self.modify = Modification(self.data.airportList, self.data.cityToCode)

    def test_remove_city(self):
        self.modify.remove_city("Santiago")
        self.assertEqual(self.data.cityToCode['SCL'], -1)

    def test_remove_route(self):
        self.modify.remove_route("Hong Kong", "Ho Chi Minh City")
        self.assertEqual(self.data.airportList['HKG'].routes['SGN'], -1)

    def test_add_city(self):
        self.modify.add_city("EC", "Edward", "USA", "Undiscovered", 6, {'N': 32, 'W': 28}, 1000000, 2)
        self.assertEqual(self.data.cityToCode["edward"], "EC")
        self.assertEqual(self.data.airportList['EC'].country, "USA")
        self.assertEqual(self.data.airportList['EC'].region, 2)


    def test_edit_coordinate(self):
        self.modify.edit_coordinate("Chicago", 'S 20 N 50')
        self.assertEqual(self.data.airportList['CHI'].coordinate, {'S': 20, 'N': 50})

    def test_edit_population(self):
        self.modify.edit_population("Chicago", 333333)
        self.assertEqual(self.data.airportList['CHI'].population, 333333)

    def test_edit_region(self):
        self.modify.edit_region("Chicago", 33)
        self.assertEqual(self.data.airportList['CHI'].region, 33)

    def test_edit_country(self):
        self.modify.edit_country("Chicago", "China")
        self.assertEqual(self.data.airportList['CHI'].country, "China")

    def test_edit_timezone(self):
        self.modify.edit_timezone("Chicago", 9)
        self.assertEqual(self.data.airportList['CHI'].timezone, 9)

    def test_edit_continent(self):
        self.modify.edit_continent("Chicago", "lol")
        self.assertEqual(self.data.airportList['CHI'].continent, "lol")

    def test_edit_code(self):
        self.modify.edit_code("Chicago", "lol")
        self.assertEqual(self.data.cityToCode['chicago'], 'lol')