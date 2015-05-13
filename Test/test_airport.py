from unittest import TestCase

from Source.Airport import Airport

__author__ = 'Edward'


class TestAirport(TestCase):

    def test_init(self):
        ap = Airport('UIUC', 'UofI', 'USA', 'North America', '+6', 'IDK', 30000, 1)
        self.assertEqual(ap.code, 'UIUC')
        self.assertEqual(ap.name, 'UofI')
        self.assertEqual(ap.country, 'USA')
        self.assertEqual(ap.continent, 'North America')
        self.assertEqual(ap.timezone, '+6')
        self.assertEqual(ap.coordinate, 'IDK')
        self.assertEqual(ap.population, 30000)
        self.assertEqual(ap.region, 1)
