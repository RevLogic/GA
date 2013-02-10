# Simple ALU implementation based on: http://revlib.org/function_details.php?id=9
# Inputs:
#    a, b := operands
#    c0, c1, c2, := operator definition, based on the following table:
#
#    0 0 0 -> constant 1
#    0 0 1 -> a OR b
#    0 1 0 -> -a OR -b
#    0 1 1 -> (a AND -b) OR (-a AND b)
#    1 0 0 -> (a AND b) OR (-a AND -b)
#    1 0 1 -> a AND b
#    1 1 0 -> -a AND -b
#    1 1 1 -> constant 0

from revsim import *

a = arg(1)
b = arg(2)
c0 = arg(3)
c1 = arg(4)
c2 = arg(5)

lines = [c0, c1, c2, a, b]
c = Cascade(lines)
c.append(tof, [2], 1)
c.append(tof, [2], 0)
c.append(tof, [1,3,4], 2)
c.append(tof, [4], 3)
c.append(tof, [0, 3], 2)
c.append(inv, [2], 2)
out = c.run()

print "f(a,b): ", out[2]
