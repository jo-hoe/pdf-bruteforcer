from src.passwordgenerator import DatesGenerator
from datetime import datetime
import unittest


class TestDatesGenerator(unittest.TestCase):

    def test_date_generator(self):
        generator = DatesGenerator(
            startdate=datetime(1990, 12, 13), 
            enddate=datetime(1990, 12, 15), 
            format="%d%m%Y")

        expected = ["13121990", "14121990", "15121990"]
        actual = []

        for item in generator.get_next_password():
            actual.append(item)

        self.assertListEqual(actual, expected)

    def test_date_end_before_startgenerator(self):
        generator = DatesGenerator(
            startdate=datetime(1990, 12, 15), 
            enddate=datetime(1990, 12, 13), 
            format="%d%m%Y")

        expected = []
        actual = []

        for item in generator.get_next_password():
            actual.append(item)

        self.assertListEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()