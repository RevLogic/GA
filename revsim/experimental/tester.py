from cascade import *
from truth_table import *

lines = {'a':True, 'b':True, 'c':False}
c = Cascade(lines)
c.append(Toffoli(['a', 'b'], 'c'))

print "Toffoli Truth Table:"

t = TruthTable(c)
print t


d = Cascade(lines)
d.append(Fredkin(['a'], ['b', 'c']))

print "Fredkin Truth Table:"
s = TruthTable(d)
print s

print "Swap Truth Table:"
e = Cascade({'a': 0, 'b':0})
e.append(Swap([], ['a', 'b']))
v = TruthTable(e)
print v
