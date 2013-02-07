from revsim import *

def binary_iterator(num_vars):
    max_val = 2 ** num_vars - 1
    bits = len(bin(max_val))

    for i in range(max_val + 1):
        bit_list = []
        current_bits = bin(i)
        for j in range(2, len(current_bits)):
            # This is terrible
            bit_list.append(int(current_bits[j]))
        # Return bitlist prepended with zeros
        yield [0]*(bits-len(current_bits)) + bit_list

