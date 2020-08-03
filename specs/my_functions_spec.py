import unittest
from my_functions import *
# can import a specific function
# from my_functions import greet

class FunctionsPracticeTest(unittest.TestCase):
    def test_greet(self):
        greeting = greet("Mark", "morning")
        self.assertEqual(greeting, "Good morning, Mark")

    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()