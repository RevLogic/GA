from cascade import *

lines = {'a':True, 'b':True, 'c':False}
c = Cascade(lines)
c.append(Toffoli(['a', 'b'], 'c'))
c.append(Toffoli(['a'], 'b'))
c.append(Toffoli(['a', 'b'], 'c'))
c.append(Toffoli(['a'], 'b'))
c.append(Toffoli(['a', 'b'], 'c'))
c.append(Toffoli(['a'], 'b'))
c.append(Toffoli(['a', 'b'], 'c'))
c.append(Toffoli(['a'], 'b'))

print "length of c", len(c)

d = Cascade(lines)
d.append(Toffoli(['a', 'b'], 'c'))
d.append(Toffoli(['a'], 'b'))
d.append(Toffoli(['a'], 'b'))
d.append(Toffoli(['a'], 'b'))
d.append(Toffoli(['a'], 'b'))
d.append(Toffoli(['a'], 'b'))
d.append(Toffoli(['a'], 'b'))
d.append(Toffoli(['a'], 'b'))

print "length of d", len(d)

e = Cascade(lines)
e = c.crossover(d)
for gate in e:
    print gate

print len(e)
print c.run()
print d.run()
print e.run()

print "C quantum cost:", c.cost()
print "D quantum cost:", d.cost()
print "E quantum cost:", e.cost()
