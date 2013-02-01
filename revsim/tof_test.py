import sys
from revsim import *

a = int(sys.argv[1])
b = int(sys.argv[2])
lines = [a, b, 0, 0]
c = Cascade(lines)
c.append(tof, [0, 1], 2)
c.append(tof, [0], 3)
c.append(tof, [1], 3)
print c.run()
