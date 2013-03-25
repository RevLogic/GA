from revsim import *
import sys

lines = {'x0':0,  'x1':0,  'x2':0,  'x3':0, 'x4':0,   'x5':0, 
         'x6':0,  'x7':0,  'x8':0,  'x9':0, 'x10': 0, 'x11':0,
         'x12':0, 'x13':0, 'x14':0, 'x15':0, 'x16':0, 'x17':0,
         'x18':0, 'x19':0, 'x20':0, 'x21':1, 'x22':0, 'x23':0, 
         'x24':1, 'x25':0, 'x26':0}

c = Cascade(lines, sorted(lines.keys())[9:int(sys.argv[1])])
"""

    c.append(Toffoli(['d','e'], 'f'))
    c.append(Toffoli(['f','g'], 'j'))
    c.append(Toffoli(['b','c','d','e','f'], 'g'))
    c.append(Toffoli(['a','c','e','g','i'], 'j'))

"""

c.append(Toffoli(['x0'], 'x9'))
c.append(Toffoli(['x0', 'x8'], 'x9'))
c.append(Toffoli(['x8'], 'x9'))
c.append(Toffoli(['x7'], 'x10'))
c.append(Toffoli(['x7', 'x9'], 'x10'))
c.append(Toffoli(['x9'], 'x10'))
c.append(Toffoli(['x0', 'x8'], 'x11'))
c.append(Toffoli(['x11'], 'x12'))
c.append(Toffoli(['x7', 'x9'], 'x12'))
c.append(Toffoli(['x7', 'x11'], 'x12'))
c.append(Toffoli(['x12'], 'x13'))
c.append(Toffoli(['x1', 'x10'], 'x13'))
c.append(Toffoli(['x1', 'x12'], 'x13'))
c.append(Toffoli(['x7', 'x11'], 'x14'))
c.append(Toffoli(['x14'], 'x15'))
c.append(Toffoli(['x1', 'x12'], 'x15'))
c.append(Toffoli(['x1', 'x14'], 'x15'))
c.append(Toffoli(['x15'], 'x16'))
c.append(Toffoli(['x6', 'x13'], 'x16'))
c.append(Toffoli(['x6', 'x15'], 'x16'))
c.append(Toffoli(['x1', 'x14'], 'x17'))
c.append(Toffoli(['x17'], 'x18'))
c.append(Toffoli(['x6', 'x15'], 'x18'))
c.append(Toffoli(['x6', 'x17'], 'x18'))
c.append(Toffoli(['x18'], 'x19'))
c.append(Toffoli(['x2', 'x16'], 'x19'))
c.append(Toffoli(['x2', 'x18'], 'x19'))
c.append(Toffoli(['x1'], 'x20'))
c.append(Toffoli(['x1', 'x10'], 'x20'))
c.append(Toffoli(['x10'], 'x20'))
c.append(Toffoli(['x6'], 'x21'))
c.append(Toffoli(['x20'], 'x21'))
c.append(Toffoli(['x6', 'x17'], 'x21'))
c.append(Toffoli(['x6', 'x20'], 'x21'))
c.append(Toffoli(['x21'], 'x22'))
c.append(Toffoli(['x2', 'x18'], 'x22'))
c.append(Toffoli(['x2', 'x21'], 'x22'))
c.append(Toffoli(['x22'], 'x23'))
c.append(Toffoli(['x5', 'x19'], 'x23'))
c.append(Toffoli(['x5', 'x22'], 'x23'))
c.append(Toffoli(['x13'], 'x20'))
c.append(Toffoli(['x6', 'x20'], 'x13'))
c.append(Toffoli(['x2'], 'x24'))
c.append(Toffoli(['x13'], 'x24'))
c.append(Toffoli(['x2', 'x21'], 'x24'))
c.append(Toffoli(['x2', 'x13'], 'x24'))
c.append(Toffoli(['x24'], 'x25'))
c.append(Toffoli(['x5', 'x22'], 'x25'))
c.append(Toffoli(['x5', 'x24'], 'x25'))
c.append(Toffoli(['x25'], 'x26'))
c.append(Toffoli(['x4', 'x23'], 'x26'))
c.append(Toffoli(['x4', 'x25'], 'x26'))
c.append(Toffoli(['x16'], 'x13'))
c.append(Toffoli(['x2', 'x13'], 'x16'))
c.append(Inverter('x16'))
c.append(Toffoli(['x5', 'x16'], 'x24'))
c.append(Toffoli(['x5', 'x24'], 'x16'))
c.append(Toffoli(['x16'], 'x25'))
c.append(Toffoli(['x4', 'x25'], 'x16'))
c.append(Toffoli(['x16'], 'x26'))
c.append(Toffoli(['x3', 'x26'], 'x16'))
c.append(Inverter('x16'))

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
print "  Calculated", 2**c.logical_width(), "cascade perms on"
print " ", len(lines), "lines and", len(c), "gates in:"
