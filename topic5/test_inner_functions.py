""" Test  file"""
import unittest

from topic5 import inner_functions_assignment


class MyTestCase(unittest.TestCase):
    def test_measurements_area(self):
        self.assertEqual(inner_functions_assignment.measurements([4, 3.4]), 'Area  = 13.6','Perimeter  = 14.8')


if __name__ == '__main__':
    unittest.main()