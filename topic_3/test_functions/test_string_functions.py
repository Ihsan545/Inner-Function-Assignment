import unittest
from topic_3.more_functions import string_functions

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertTrue("Good!", string_functions.multiply_string(5))


if __name__ == '__main__':
    unittest.main()
