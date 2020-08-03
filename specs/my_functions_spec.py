import unittest
from my_functions import *

class FunctionsPracticeTest(unittest.TestCase):
    def test_greet(self):
        greeting = greet("Mark", "morning")
        self.assertEqual(greeting, "Good morning, Mark")

if __name__ == "__main__":
    unittest.main()