from revsim import *
from perms import *

lines = [0,1,1,0,0,1,0,0,0,1,0]
c = Cascade(lines)
print "Constructing Cascade..."
for i in range(0, 2000):
    c.append(toffoli, [0,1], 2)
    c.append(toffoli, [1,2], 3)
    c.append(toffoli, [2,3], 4)
    c.append(toffoli, [3,4], 5)
    c.append(toffoli, [4,5], 6)
    c.append(toffoli, [1,2,3,4,5], 6)
    c.append(toffoli, [0,2,4,6,8], 9)

print "Running..."
print c.run()
print "Length of cascade:", len(c)
c.write_pickle("massive.pckl")
print "Quantum Cost:", c.quantum_cost()

print ""
print "Loading 1000 Cascades into RAM..."
cascadeList = []
for i in range(0, 1000):
    cascadeList.append(Cascade(lines, "test_massive.pckl"))

# This part took about 4 minutes to run on linux1... not bad
print ""
print "Simulating 2^10 input perms..."
i = 1
for perm in binary_iterator(10):
    lines = perm
    c.replace_lines(lines)
    c.run()
    i += 1

print "Done!"
