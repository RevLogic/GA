from revsim import *

num_vars = 4
max_val = 2 ** num_vars
bits = len(bin(max_val))

for i in range(max_val):
    bit_list = []
    current_bits = bin(i)
    for j in range(2, len(current_bits)):
        # This is terrible
        bit_list.append(int(current_bits[j]))
    # Return bitlist prepended with zeros
    print [0]*(bits-len(current_bits)) + bit_list
