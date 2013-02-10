# RevSim Test Toolkit
# Christopher Rabl
# This test file implements the circuit: http://revlib.org/doc/real/4mod7-v0_95.real

from revsim import *

b = arg(1)
c = arg(2)
d = arg(3)
e = arg(4)
lines = [0, b, c, d, e]
c = Cascade(lines)
c.append(tof, [1,4], 0)
c.append(tof, [1], 4)
c.append(tof, [2,3,4], 0)
c.append(tof, [0,2,3], 4)
c.append(tof, [0, 3], 2)
c.append(tof, [0], 3)

out = c.run()

print "c: ", out[2]
print "d: ", out[3]
print "e: ", out[4]
