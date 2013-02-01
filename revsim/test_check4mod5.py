import sys
from revsim import *

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = int(sys.argv[4])
lines = [a, b, c, int(not(d)), 0]

c = Cascade(lines)
c.append(tof, [1], 3)
c.append(tof, [3], 4)
c.append(tof, [2,3], 4)
c.append(tof, [0,3], 4)

print c.run()
