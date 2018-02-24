import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
    def test_exponent(self):
    	result = rpn.calculate("2 2 ^")
    	self.assertEqual(4, result)
    def test_rotate(self):
        result = rpn.calculate("1 2 3 4 5 6 7 rotate")
        self.assertEqual([7, 6, 5, 4, 3, 2, 1], result)
        result = rpn.calculate("99 555 3 rotate")
        self.assertEqual([3, 555, 99], result)
        result = rpn.calculate("7 6 5 4 3 2 1 rotate")
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], result)
        result = rpn.calculate("2 4 6 rotate")
        self.assertEqual([6, 4, 2], result)
    # def test_copy(self):
    #     result = rpn.calculate("2 4 6 copy")
    #     self.assertEqual([2, 2, 4, 6], result)
    #     result = rpn.calculate("4 66 4 copy")
    #     self.assertEqual([4, 4, 66, 4], result)
    def test_factorial(self):
        # print("testing factorial function...")
        result = rpn.calculate("4 !")
        self.assertEqual(24, result)
        result = rpn.calculate("8 !")
        self.assertEqual(40320, result)
        result = rpn.calculate("5 !")
        self.assertEqual(120, result)