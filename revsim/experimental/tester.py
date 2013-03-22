from cascade import *
from truth_table import *

lines = {'a':True, 'b':True, 'c':False}
c = Cascade(lines)
c.append(Toffoli(['a', 'b'], 'c'))

print "C Truth Table:"

t = TruthTable(c)
print t


d = Cascade(lines)
d.append(Fredkin(['a'], ['b', 'c']))

print "D Truth Table:"
s = TruthTable(d)
print s

