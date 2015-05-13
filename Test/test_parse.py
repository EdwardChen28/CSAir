from unittest import TestCase

from Source.Parse import Parse

__author__ = 'Edward'


class TestParse(TestCase):
    def test_parse_data(self):
        p = Parse("../UI/data.json")
        # total 48 airport
        self.assertEqual(len(p.airportList), 48)
        self.assertEqual(len(p.cityToCode), 48)
        self.assertEqual(p.airportList['SCL'].name, 'Santiago')
        self.assertEqual(p.airportList['CHI'].name, 'Chicago')
        self.assertEqual(p.airportList['MEX'].routes['LAX'], 2499)

        # read another file
        p.parse_data("../UI/cmi_hub.json")
        self.assertEqual(p.airportList['CMI'].name, 'Champaign')
        self.assertEqual(p.airportList['CMI'].country, 'US')
        self.assertEqual(p.airportList['CMI'].continent, 'North America')
        self.assertEqual(p.airportList['CMI'].population, 226000)
        self.assertEqual(len(p.airportList['CMI'].routes), 9)