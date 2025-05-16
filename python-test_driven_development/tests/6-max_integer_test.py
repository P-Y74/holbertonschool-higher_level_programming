"""
Unittest module for the function max_integer.

This module contains test cases for the function max_integer, which returns
the maximum value in a list of integers. The tests cover multiple edge cases,
including empty lists, lists with one element, strings, None, and invalid types.
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defines a test case for the max_integer function."""
    def test_order_list(self):
        """Test with a list of integers in increasing order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reverse_list(self):
        """Test with a list of integers in decreasing order."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_element(self):
        """Test with a list containing only one element."""
        self.assertEqual(max_integer([2]), 2)

    def test_empty_list(self):
        """Test with an empty list should return None."""
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        """Test with a list of only negative integers."""
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
    
    def test_positive_negative_numbers(self):
        self.assertEqual(max_integer([-3, 1, 0, -7]), 1)
        """Test with a list containing both positive
        and negative integers."""
    
    def test_string_list(self):
        self.assertEqual(max_integer(["a", "z", "c"]), "z")
        """Test with a list of strings; should return
        the max string (lexicographically)."""
    
    def test_mix_type(self):
        with self.assertRaises(TypeError):
            max_integer([1, "a", 3.5])
            """Test with a list containing mixed
            types should raise TypeError."""

    def test_none_element(self):
        with self.assertRaises(TypeError):
            max_integer(None)
            """Test passing None as argument should raise TypeError."""

    def test_none_list(self):
        with self.assertRaises(TypeError):
            max_integer(None)
            """Test again with None to verify consistent TypeError handling."""

    def test_no_argument(self):
        self.assertEqual(max_integer(), None)
        """Test calling max_integer with no argument; should return None."""

if __name__ == "__main__":
    unittest.main()
