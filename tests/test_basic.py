import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from Basics.main import add_numbers
class TestBasics(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual("Hello World!","Hello World!")

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2,3),5)

if __name__ == "__main__":
    unittest.main()