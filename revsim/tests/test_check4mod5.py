from revsim import *

a = arg(1)
b = arg(2)
c = arg(3)
d = arg(4)
lines = [a, b, c, d, 0]

c = Cascade(lines)
c.append(inv, [3], 3)
c.append(tof, [1], 3)
c.append(tof, [3], 4)
c.append(tof, [2,3], 4)
c.append(tof, [0,3], 4)

print c.run()
