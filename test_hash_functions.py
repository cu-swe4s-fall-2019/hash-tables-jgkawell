import unittest
import hash_functions
import random
import os
import numpy as np


class TestHashFunctions(unittest.TestCase):

    def test_ascii_basic(self):
        test = "Hello World"
        table_size = 100
        self.assertGreater(hash_functions.h_ascii(test, table_size), 0)

    def test_ascii_empty_string(self):
        test = ""
        table_size = 100
        self.assertEqual(hash_functions.h_ascii(test, table_size), 0)

    def test_ascii_key_non_string(self):
        test = 3.14
        table_size = 100
        self.assertEqual(hash_functions.h_ascii(test, table_size), -1)

    def test_ascii_table_size_non_num(self):
        test = "Hello World"
        table_size = "not number"
        self.assertEqual(hash_functions.h_ascii(test, table_size), -1)

    def test_rolling_basic(self):
        test = "Hello World"
        table_size = 100
        self.assertGreater(hash_functions.h_rolling(test, table_size), 0)

    def test_rolling_empty_string(self):
        test = ""
        table_size = 100
        self.assertEqual(hash_functions.h_rolling(test, table_size), 0)

    def test_rolling_key_non_string(self):
        test = 3.14
        table_size = 100
        self.assertEqual(hash_functions.h_rolling(test, table_size), -1)

    def test_rolling_table_size_non_num(self):
        test = "Hello World"
        table_size = "not number"
        self.assertEqual(hash_functions.h_rolling(test, table_size), -1)

    def test_rolling_p_non_num(self):
        test = "Hello World"
        table_size = 100
        p = "not number"
        self.assertEqual(hash_functions.h_rolling(test, table_size, p=p), -1)

    def test_rolling_m_non_num(self):
        test = "Hello World"
        table_size = "not number"
        m = "not number"
        self.assertEqual(hash_functions.h_rolling(test, table_size, m=m), -1)


if __name__ == '__main__':
    unittest.main()
