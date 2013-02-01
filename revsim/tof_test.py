from tof import *

lines = [0, 0, 0, 0]
lines = apply(lines, tof, [0,1], 3)
print lines     
lines = apply(lines, tof, [0], 1)
print lines
lines = apply(lines, tof, [1,2], 3)
print lines
lines = apply(lines, tof, [1], 2)
print lines

print "sum: ", lines[2]
print "car: ", lines[3]
