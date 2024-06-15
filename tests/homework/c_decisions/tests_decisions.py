#
import unittest
from src.homework.c_decisions.decisions import get_options_ratio, get_faculty_rating

class Test_Config(unittest.TestCase):

    def test_get_options_ratio(self):
        # Test case for get_options_ratio with values 5 and 20, expecting .25
        self.assertAlmostEqual(get_options_ratio(5, 20), 0.25)
        # Test case for get_options_ratio with values 10 and 20, expecting .5
        self.assertAlmostEqual(get_options_ratio(10, 20), 0.5)
        # Additional test case to ensure ValueError is raised for division by zero
        with self.assertRaises(ValueError):
            get_options_ratio(5, 0)

    def test_get_faculty_rating(self):
        # Test case for get_faculty_rating with ratio .91, expecting 'Excellent'
        self.assertEqual(get_faculty_rating(0.91), 'Excellent')
        # Test case for get_faculty_rating with ratio .85, expecting 'Very Good'
        self.assertEqual(get_faculty_rating(0.85), 'Very Good')
        # Test case for get_faculty_rating with ratio .71, expecting 'Good'
        self.assertEqual(get_faculty_rating(0.71), 'Good')
        # Test case for get_faculty_rating with ratio .66, expecting 'Needs Improvement'
        self.assertEqual(get_faculty_rating(0.66), 'Needs Improvement')
        # Test case for get_faculty_rating with ratio .45, expecting 'Unacceptable'
        self.assertEqual(get_faculty_rating(0.45), 'Unacceptable')

# To run the tests
if __name__ == '__main__':
    unittest.main()
