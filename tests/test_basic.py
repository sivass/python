import unittest

class TestBasics(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual("Hello World!","Hello World")

    def test_add_numbers(self):
        from Basics import add_numbers
        self.assertEqual(add_numbers(2,3),5)

if __name__ == "__main__":
    unittest.main()