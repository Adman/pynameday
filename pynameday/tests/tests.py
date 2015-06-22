from unittest import TestCase
from pynameday.slovakia import Slovakia
from pynameday.czechrepublic import CzechRepublic
from pynameday.austria import Austria


class NamedayMixinTest(object):
    MONTHS = 12
    DAYS = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    cal = None

    def test_months(self):
        self.assertEqual(len(self.cal), self.MONTHS)

    def test_days(self):
        for i, j in enumerate(self.cal):
            self.assertEqual(len(j), self.DAYS[i])


class SlovakiaTest(TestCase, NamedayMixinTest):
    """Slovakian nameday test"""
    def setUp(self):
        self.cal = Slovakia.NAMEDAYS


class CzechRepublicTest(TestCase, NamedayMixinTest):
    """Czech nameday test"""
    def setUp(self):
        self.cal = CzechRepublic.NAMEDAYS


class AustriaTest(TestCase, NamedayMixinTest):
    """Austrian nameday test"""
    def setUp(self):
        self.cal = Austria.NAMEDAYS
