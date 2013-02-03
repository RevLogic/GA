from revsim import *

maxVal = 16
for i in range(maxVal):
    n = len(bin(maxVal))
    binList = []
    for j in range(2, len(bin(i))):
        # This is terrible
        binList.append(int(bin(i)[j]))
    # Return bitlist prepended with zeros
    print [0]*(n-len(bin(i))) + binList
