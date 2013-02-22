# Author: Christopher Rabl
# Description: Outputs 1 on the last line if the majority (>= 2/3) of the inputs are 1

from revsim import *
from perms import *

# This answers Q2a of Exercise 4

lines = [0, 0, 0, 0]
c = Cascade(lines)
c.append(toffoli, [0,1], 3)
c.append(toffoli, [0,2], 3)
c.append(toffoli, [1,2], 3)

for perm in binary_iterator(3):
    lines = perm + [0]
    c.replace_lines(lines)
    print lines, "->", c.run()

# Using the shiny new __iter__ method, our Cascades are now iterable!
for item in c:
    print item

print ""
print c[1]
