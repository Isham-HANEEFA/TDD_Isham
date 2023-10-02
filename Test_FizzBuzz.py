import unittest
from FizzBuzz import *

class Test_FizzBuzz(unittest.TestCase):

    def setUp(self):
        self.instance=FizzBuzz()


    def test_affiche(self):
        self.assertEqual(self.instance.affiche(10), "12Fizz4BuzzFizz78FizzBuzz")
        self.assertEqual(self.instance.affiche(5), "12Fizz4Buzz")


if __name__ == '__main__':
    unittest.main()