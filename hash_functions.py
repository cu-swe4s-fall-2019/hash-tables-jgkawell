import argparse


def h_ascii(key, table_size):
    """
    Generates a hash from the given key by summing ASCII values.

    Parameters
    ----------
    key : a string to hash
    table_size : a number representing the size of the hash table
    p : a prime number roughly the number of characters in the input alphabet
    m : a large number, since the probability of two random strings colliding
        is about 1/m. Sometimes m=2^64 is chosen.

    Returns
    ----------
    hash : the hashed string or -1 for failure
    """

    # Check for key as string
    if isinstance(key, str):
        # Sum up all the ASCII values
        total = 0
        for element in key:
            total += ord(element)
        # Try to return modulo table_size
        try:
            return total % table_size
        except TypeError:
            print("ERROR: Must pass a number as the table size.")
    else:
        print("ERROR: Must pass a string as the key to hash function.")

    # Return error code
    return -1


def h_rolling(key, table_size, p=53, m=2**64):
    """
    Generates a polynomial rolling hash from the given key.

    Parameters
    ----------
    key : a string to hash
    table_size : a number representing the size of the hash table
    p : a prime number roughly the number of characters in the input alphabet
    m : a large number, since the probability of two random strings colliding
        is about 1/m. Sometimes m=2^64 is chosen.

    Returns
    ----------
    hash : the hashed string or -1 for failure
    """

    # Check for key as string
    if isinstance(key, str):
        try:
            # Sum up all the ASCII values with a rolling polynomial multiple
            total = 0
            for i in range(len(key)):
                total += ord(key[i]) * p**i
            total = total % m
            # Try to return modulo table_size
            return total % table_size
        except TypeError:
            print("ERROR: Must pass a numbers for table_size, p, and m.")
    else:
        print("ERROR: Must pass a string as the key to hash function.")

    # Return error code
    return -1


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Calculate hash data from a file.')
    parser.add_argument(
        '--input_file',
        type=str,
        help='The file name of the data')
    parser.add_argument(
        '--hash_function',
        type=str,
        help='The function name of the hash type')

    args = parser.parse_args()

    for l in open(args.input_file):
        if args.hash_function == 'ascii':
            print(h_ascii(l, 1000))
        elif args.hash_function == 'rolling':
            print(h_rolling(l, 1000))
