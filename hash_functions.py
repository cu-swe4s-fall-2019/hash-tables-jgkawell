
def h_ascii(key, table_size):
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
