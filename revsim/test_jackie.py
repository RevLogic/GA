from revsim import *

# Implements Jackie's one-bit adder detailed in class

a = arg(1)
b = arg(2)
lines = [a, b, 0, 0]

c = Cascade(lines)
c.append(tof, [0, 1], 2)
c.append(tof, [0], 3)
c.append(tof, [1], 3)
output = c.run(True)

print "Carry: ", output[2]
print "Sum: ", output[3]
