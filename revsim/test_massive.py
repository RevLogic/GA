from revsim import *
from perms import *

lines = {'a':0, 'b':1, 'c':1, 'd':0, 'e':0, 'f':1, 'g':0, 'h':0, 'i':0, 'j':1}
c = Cascade(lines)
print "Constructing Cascade..."
for i in range(0, 2000):
    c.append(toffoli, ['a','b'], 'c')
    c.append(toffoli, ['b','c'], 'd')
    c.append(toffoli, ['c','d'], 'e')
    c.append(toffoli, ['d','e'], 'f')
    c.append(toffoli, ['f','g'], 'h')
    c.append(toffoli, ['b','c','d','e','f'], 'g')
    c.append(toffoli, ['a','c','e','g','i'], 'j')

print "Running..."
print c.run()
print "Length of cascade:", len(c)
c.write_pickle("massive.pckl")
print "Quantum Cost:", c.quantum_cost()

d = c.copy()
print "D quantum Cost:", d.quantum_cost()

# DO NOT RUN THIS UNLESS YOU HAVE OVER A GIG OF RAM TO SPARE !!!!!
"""
print ""
print "Copying 1000 Cascades from RAM..."
cascadeList = []
for i in range(0, 1000):
    cascadeList.append(c.copy())
    print i


# DO NOT RUN THIS UNLESS YOU HAVE EVEN MORE RAM TO SPARE !!!!!

print ""
print "Loading 1000 Cascades into RAM from disk..."
cascadeList2 = []
for i in range(0, 1000):
    cascadeList2.append(Cascade(lines, "massive.pckl"))
    print i
"""
"""
# This part took about 4 minutes to run on linux1... not bad
print ""
print "Simulating 2^10 input perms..."
i = 1
for perm in binary_iterator(10):
    lines = dict(zip(['a','b','c','d','e','f','g','h','i','j'], perm))
    c.replace_lines(lines)
    print c.run(), i
    i += 1
"""

# Takes about 2 minutes
c.permutation_matrix()

print "Done!"
