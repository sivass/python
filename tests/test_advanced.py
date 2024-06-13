import unittest

class TestAdvanced(unittest.TestCase):
    def test_list_comprehension(self):
        squares = [x**2 for x in range(10)]
        self.assertEqual(squares, [0,1,4,9,16,25,36,49,64,81])
    
    def test_apply_func(self):
        from Advanced import apply_func, square
        self.assertEqual(apply_func(square,5),25)

if __name__ == '__main__':
    unittest.main()