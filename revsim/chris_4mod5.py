from revsim import *
from perms import *

lines = [0, 0, 0, 0, 0]

c = Cascade(lines)
# Case 0: 0 0 0 0
c.append(inverter, [0], 0)
c.append(inverter, [1], 1)
c.append(inverter, [2], 2)
c.append(inverter, [3], 3)
c.append(toffoli, [0,1,2,3], 4)
c.append(inverter, [0], 0)
c.append(inverter, [2], 2)

# Case 5: 0 1 0 1
c.append(toffoli, [0,1,2,3], 4)
c.append(inverter, [1], 1)
c.append(inverter, [3], 3)

# Case 10: 1 0 1 0
c.append(inverter, [0], 0)
c.append(inverter, [2], 2)
c.append(toffoli, [0,1,2,3], 4)
c.append(inverter, [0], 0)
c.append(inverter, [2], 2)

# Case 15: 1 1 1 1
c.append(toffoli, [0,1,2,3], 4)

for perm in binary_iterator(4):
    lines = perm + [0]
    c.replace_lines(lines)
    revlines = c.run()
    c.replace_lines(revlines)
    print lines, revlines, c.run()

print "Quantum cost:", c.quantum_cost()
