import unittest
from topic_4 import validate_input_in_function


class MyTestCase(unittest.TestCase):
    def test_score_valid(self):
        self.assertTrue(validate_input_in_function.score_input("python", 7))

    def test_above_range_input(self):
        self.assertTrue(validate_input_in_function.score_input("Invalid value, above the range"), 245)




if __name__ == '__main__':
    unittest.main()