import perms
from revsim import *

# Create a new binary perm iterator
line_perms = perms.binary_iterator(3)

c = Cascade([0, 0, 0])
c.append(tof, [0,1], 2)

#d = Cascade([0, 0, 0])
#d.append(tof, [0,1], 2)

# Run through every input permutation and output
# the gate results at every step
for perm in line_perms:
    c.replace_lines(perm)
    #d.replace_lines(perm)
    print c.run()
    print c.run()
    #if c.run() != d.run():
        #print "NO"
    print ""


print "YES"

