import unittest
import hash_functions
import random
import os
import numpy as np

class TestHashFunctions(unittest.TestCase):

    def test_ascii_basic(self):
        test_string = "Hello World"
        table_size = 100
        self.assertGreater(hash_functions.h_ascii(test_string, table_size), 0)

    def test_ascii_empty_string(self):
        test_string = ""
        table_size = 100
        self.assertEqual(hash_functions.h_ascii(test_string, table_size), 0)

    def test_ascii_key_non_string(self):
        test_string = 3.14
        table_size = 100
        self.assertEqual(hash_functions.h_ascii(test_string, table_size), -1)

    def test_ascii_table_size_non_num(self):
        test_string = "Hello World"
        table_size = "not number"
        self.assertEqual(hash_functions.h_ascii(test_string, table_size), -1)


if __name__ == '__main__':
    unittest.main()
