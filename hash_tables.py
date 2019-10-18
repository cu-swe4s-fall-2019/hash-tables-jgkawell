from hash_functions import h_ascii
from hash_functions import h_rolling


class LinearProbe:
    def __init__(self, table_size, hash_function):
        self.hash_function = hash_function
        self.table_size = table_size
        try:
            self.table = [None for i in range(self.table_size)]
        except TypeError:
            print(
                "WARN: Must pass a number as the table size. Default: 1000.")
            self.table_size = 1000
            self.table = [None for i in range(self.table_size)]
        self.num_elements = 0

    def add(self, key, value):
        try:
            hash_slot = self.hash_function(key, self.table_size)
        except TypeError:
            print("ERROR: hash_function must be valid Python function name.")
            return False

        # Make sure that the slot is valid
        if hash_slot >= 0:
            for i in range(self.table_size):
                test_slot = (hash_slot + i) % self.table_size
                if self.table[test_slot] is None:
                    self.table[test_slot] = (key, value)
                    self.num_elements += 1
                    return True

        return False

    def search(self, key):
        try:
            hash_slot = self.hash_function(key, self.table_size)
        except TypeError:
            print("ERROR: hash_function must be valid Python function name.")
            return None

        # Make sure that the slot is valid
        if hash_slot >= 0:
            for i in range(self.table_size):
                test_slot = (hash_slot + i) % self.table_size
                if self.table[test_slot] is None:
                    return None
                if self.table[test_slot][0] == key:
                    return self.table[test_slot][1]

        return None


class ChainedHash:
    def __init__(self, table_size, hash_function):
        self.hash_function = hash_function
        self.table_size = table_size
        try:
            self.table = [[] for i in range(self.table_size)]
        except TypeError:
            print(
                "WARN: Must pass a number as the table size. Default: 1000.")
            self.table_size = 1000
            self.table = [[] for i in range(self.table_size)]
        self.num_elements = 0

    def add(self, key, value):
        try:
            hash_slot = self.hash_function(key, self.table_size)
        except TypeError:
            print("ERROR: hash_function must be valid Python function name.")
            return False

        self.table[hash_slot].append((key, value))
        self.num_elements += 1
        return True

    def search(self, key):
        try:
            hash_slot = self.hash_function(key, self.table_size)
        except TypeError:
            print("ERROR: hash_function must be valid Python function name.")
            return None

        for k, v in self.table[hash_slot]:
            if key == k:
                return v
        return None
