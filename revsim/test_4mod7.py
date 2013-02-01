# RevSim Test Toolkit
# Christopher Rabl
# This test file implements the circuit: http://revlib.org/doc/real/4mod7-v0_95.real

import sys
from revsim import *

b = int(sys.argv[1])
c = int(sys.argv[2])
d = int(sys.argv[3])
e = int(sys.argv[4])
lines = [0, b, c, d, e]
lines = apply(lines, tof, [1,4], 0)
lines = apply(lines, tof, [1], 4)
lines = apply(lines, tof, [2,3,4], 0)
lines = apply(lines, tof, [0,2,3], 4)
lines = apply(lines, tof, [0,3], 2)
lines = apply(lines, tof, [0], 3)

print "c: ", int(lines[2])
print "d: ", int(lines[3])
print "e: ", int(lines[4])
