import unittest
import hash_tables
import hash_functions as hf
import random as r
import os
import numpy as np
import string as s


class TestHashTables(unittest.TestCase):

    """ Test Linear Probe """

    def test_linear_probe_ascii_basic(self):
        size = 100
        hash_table = hash_tables.LinearProbe(size, hf.h_ascii)

        entries = {}
        for i in range(int(size / 2)):
            key = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
            value = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
            entries[key] = value
            self.assertTrue(hash_table.add(key, value))

        for k, v in entries.items():
            self.assertEqual(hash_table.search(k), v)

    def test_linear_probe_rolling_basic(self):
        size = 100
        hash_table = hash_tables.LinearProbe(size, hf.h_rolling)

        entries = {}
        for i in range(int(size / 2)):
            key = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
            value = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
            entries[key] = value
            self.assertTrue(hash_table.add(key, value))

        for k, v in entries.items():
            self.assertEqual(hash_table.search(k), v)

    def test_linear_probe_bad_function_name(self):
        size = 100
        hash_table = hash_tables.LinearProbe(size, "not function")

        key = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
        value = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
        self.assertFalse(hash_table.add(key, value))
        self.assertEqual(hash_table.search(key), None)

    def test_linear_probe_bad_size(self):
        size = "not number"
        hash_table = hash_tables.LinearProbe(size, hf.h_ascii)

        entries = {}
        for i in range(500):
            key = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
            value = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
            entries[key] = value
            self.assertTrue(hash_table.add(key, value))

        for k, v in entries.items():
            self.assertEqual(hash_table.search(k), v)

    def test_linear_probe_nonexistent_key(self):
        size = 100
        hash_table = hash_tables.LinearProbe(size, hf.h_ascii)

        entries = {}
        for i in range(int(size / 2)):
            key = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
            value = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
            entries[key] = value
            self.assertTrue(hash_table.add(key, value))

        self.assertEqual(
            hash_table.search(
                "This is a key that is very unlikely to be generated"), None)

    def test_linear_probe_rehashing(self):
        size = 100
        hash_table = hash_tables.LinearProbe(size, hf.h_ascii)

        entries = {}
        for i in range(int(size * 2)):
            key = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
            value = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
            entries[key] = value
            self.assertTrue(hash_table.add(key, value))

        for k, v in entries.items():
            self.assertEqual(hash_table.search(k), v)

    """ Test Chained Hash """

    def test_chained_hash_ascii_basic(self):
        size = 100
        hash_table = hash_tables.ChainedHash(size, hf.h_ascii)

        entries = {}
        for i in range(int(size / 2)):
            key = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
            value = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
            entries[key] = value
            self.assertTrue(hash_table.add(key, value))

        for k, v in entries.items():
            self.assertEqual(hash_table.search(k), v)

    def test_chained_hash_rolling_basic(self):
        size = 100
        hash_table = hash_tables.ChainedHash(size, hf.h_rolling)

        entries = {}
        for i in range(int(size / 2)):
            key = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
            value = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
            entries[key] = value
            self.assertTrue(hash_table.add(key, value))

        for k, v in entries.items():
            self.assertEqual(hash_table.search(k), v)

    def test_chained_hash_bad_function_name(self):
        size = 100
        hash_table = hash_tables.ChainedHash(size, "not function")

        key = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
        value = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
        self.assertFalse(hash_table.add(key, value))
        self.assertEqual(hash_table.search(key), None)

    def test_chained_hash_bad_size(self):
        size = "not number"
        hash_table = hash_tables.ChainedHash(size, hf.h_ascii)

        entries = {}
        for i in range(500):
            key = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
            value = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
            entries[key] = value
            self.assertTrue(hash_table.add(key, value))

        for k, v in entries.items():
            self.assertEqual(hash_table.search(k), v)

    def test_chained_hash_nonexistent_key(self):
        size = 100
        hash_table = hash_tables.ChainedHash(size, hf.h_ascii)

        entries = {}
        for i in range(int(size / 2)):
            key = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
            value = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
            entries[key] = value
            self.assertTrue(hash_table.add(key, value))

        self.assertEqual(
            hash_table.search(
                "This is a key that is very unlikely to be generated"), None)

    def test_chained_hash_rehashing(self):
        size = 100
        hash_table = hash_tables.ChainedHash(size, hf.h_ascii)

        entries = {}
        for i in range(int(size * 2)):
            key = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
            value = ''.join(r.choices(s.ascii_uppercase + s.digits, k=100))
            entries[key] = value
            self.assertTrue(hash_table.add(key, value))

        for k, v in entries.items():
            self.assertEqual(hash_table.search(k), v)

if __name__ == '__main__':
    unittest.main()
