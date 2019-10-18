import argparse
import copy
import random
import time

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
        # Get a hash position
        try:
            hash_slot = self.hash_function(key, self.table_size)
        except TypeError:
            print("ERROR: hash_function must be valid Python function name.")
            return False

        # Make sure that the slot is valid
        success = False
        if hash_slot >= 0:
            for i in range(self.table_size):
                test_slot = (hash_slot + i) % self.table_size
                if self.table[test_slot] is None:
                    self.table[test_slot] = (key, value)
                    self.num_elements += 1
                    success = True
                    break

        # Check load factor and rehash if needed
        if (self.num_elements / self.table_size) > 0.7:
            self.rehash()

        # If the insert failed, rehash and insert again
        if not success:
            self.rehash()
            return self.add(key, value)
        else:
            return True

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

    def rehash(self):
        # Save the old table data
        old_table_size = self.table_size
        old_table = copy.deepcopy(self.table)
        # Update table data with double the size
        self.table_size = old_table_size * 2
        self.table = [None for i in range(self.table_size)]
        # Rehash everything into the new table
        for i in range(old_table_size):
            if old_table[i] is not None:
                self.add(old_table[i][0], old_table[i][1])


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

        # Check load factor and rehash if needed
        if (self.num_elements / self.table_size) > 0.7:
            self.rehash()

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

    def rehash(self):
        # Save the old table data
        old_table_size = self.table_size
        old_table = copy.deepcopy(self.table)
        # Update table data with double the size
        self.table_size = old_table_size * 2
        self.table = [[] for i in range(self.table_size)]
        # Rehash everything into the new table
        for i in range(old_table_size):
            if len(old_table[i]) > 0:
                for k, v in old_table[i]:
                    self.add(k, v)


def reservoir_sampling(new_val, size, V):
    if len(V) < size:
        V.append(new_val)
    else:
        j = random.randint(0, len(V))
        if j < len(V):
            V[j] = new_val


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Calculate hash data from a file.')
    parser.add_argument(
        '--table_size',
        type=int,
        help='The initial size of the hash table')
    parser.add_argument(
        '--hash_alg',
        type=str,
        help='The function name of the hash type')
    parser.add_argument(
        '--collision_strategy',
        type=str,
        help='The collision strategy (linear/chain)')
    parser.add_argument(
        '--data_file_name',
        type=str,
        help='The name of the data file')
    parser.add_argument(
        '--keys_to_add',
        type=int,
        help='The number of keys to hash')

    args = parser.parse_args()

    N = args.table_size
    hash_alg = args.hash_alg
    collision_strategy = args.collision_strategy
    data_file_name = args.data_file_name
    keys_to_add = args.keys_to_add

    ht = None

    if hash_alg == 'ascii':

        if collision_strategy == 'linear':
            ht = LinearProbe(N, h_ascii)
        elif collision_strategy == 'chain':
            ht = ChainedHash(N, h_ascii)

    elif hash_alg == 'rolling':

        if collision_strategy == 'linear':
            ht = LinearProbe(N, h_rolling)
        elif collision_strategy == 'chain':
            ht = ChainedHash(N, h_rolling)

    keys_to_search = 100
    V = []

    for l in open(data_file_name):
        reservoir_sampling(l, keys_to_search, V)
        t0 = time.time()
        ht.add(l, l)
        t1 = time.time()
        print('add', ht.num_elements/ht.table_size, t1 - t0)
        if ht.num_elements == keys_to_add:
            break

    for v in V:
        t0 = time.time()
        r = ht.search(v)
        t1 = time.time()
        print('search', t1 - t0)
