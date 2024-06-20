import unittest
from tests.homework.d_repetition import tests_repetition #made change for test

suite = unittest.TestLoader().loadTestsFromModule(tests_repetition) # made change for test
unittest.TextTestRunner().run(suite)
