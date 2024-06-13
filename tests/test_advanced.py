import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from Advanced.main import apply_func, square
class TestAdvanced(unittest.TestCase):
    def test_list_comprehension(self):
        squares = [x**2 for x in range(10)]
        self.assertEqual(squares, [0,1,4,9,16,25,36,49,64,81])
    
    def test_apply_func(self):
        self.assertEqual(apply_func(square,5),25)

if __name__ == '__main__':
    unittest.main()