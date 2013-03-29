from revsim import *

lines = {'a':0, 'b':1, 'c':1, 'd':0, 'e':0, 'f':1, 'g':0, 'h':0, 'i':0, 'j':1}
c = Cascade(lines)
print "Constructing Cascade..."
for i in range(0, 2000):
    c.append(Toffoli(['a','b'], 'c'))
    c.append(Toffoli(['b','c'], 'd'))
    c.append(Toffoli(['c','d'], 'e'))
    c.append(Toffoli(['d','e'], 'f'))
    c.append(Toffoli(['f','g'], 'j'))
    c.append(Toffoli(['b','c','d','e','f'], 'g'))
    c.append(Toffoli(['a','c','e','g','i'], 'j'))

print "Running..."
print c.run()
print "Length of cascade:", len(c)
print "Quantum Cost:", c.cost()

print "Creating truth table..."
t = TruthTable(c, calc_stats=True)
print t
print "Done!"
print ""
print "  SUMMARY"
print "--------------------------------------------"
print "  Calculated", 2**len(lines), "cascade perms on"
print " ", len(lines), "lines and", len(c), "gates in:"
