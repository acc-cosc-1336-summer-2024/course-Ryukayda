import unittest
from src.homework.i_dictionaries_sets.dictionary import get_p_distance, get_p_distance_matrix

class Test_Config(unittest.TestCase):

    def test_get_p_distance(self):
        list1 = ['T','T','T','C','C','A','T','T','T','A']
        list2 = ['G','A','T','T','C','A','T','T','T','C']

        list3 = ['T','T','T','C','C','A','T','T','T','A']
        list4 = ['G','A','T','T','C','A','T','T','T','C']
        list5 = ['T','T','T','C','C','A','T','T','T','T']
        list6 = ['G','T','T','C','C','A','T','T','T','A']
        self.assertEqual(.4, get_p_distance(list1, list2))
        self.assertEqual(0.0, get_p_distance(list3, list3))
        self.assertEqual(0.1, get_p_distance(list3, list5))
        self.assertEqual(0.3, get_p_distance(list4, list6))

    def test_get_p_distance_matrix(self):
        my_val = [
        [0.0, 0.4, 0.1, 0.1],
        [0.4, 0.0, 0.4, 0.3],
        [0.1, 0.4, 0.0, 0.2],
        [0.1, 0.3, 0.2, 0.0]
        ]
        
        my_test = [
        ['T','T','T','C','C','A','T','T','T','A'],
        ['G','A','T','T','C','A','T','T','T','C'],
        ['T','T','T','C','C','A','T','T','T','T'],
        ['G','T','T','C','C','A','T','T','T','A']
        ]

        self.assertEqual(my_val, get_p_distance_matrix(my_test))