
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


def h_rolling(key, N):
    return None
