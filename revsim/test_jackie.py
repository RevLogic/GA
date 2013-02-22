from perms import *
from revsim import *

# Implements Jackie's one-bit adder detailed in class

lines = [0, 0, 0, 0]

c = Cascade(lines)
c.append(toffoli, [0, 1], 2)
c.append(toffoli, [0], 3)
c.append(toffoli, [1], 3)
c.write_pickle("jackie_adder.cas")

for perm in binary_iterator(2):
    lines = perm + [0, 0]
    c.replace_lines(lines)
    output = c.run()
    print lines
    print "Carry: ", output[2]
    print "Sum: ", output[3]
    print ""

for item in c.items():
    print item
