# Revsim experimental
# Sym9

from revsim import *

lines = {'x0':0,  'x1':0,  'x2':0,  'x3':0, 'x4':0,   'x5':0, 
         'x6':0,  'x7':0,  'x8':0,  'x9':0, 'x10': 0, 'x11':0,
         'x12':0, 'x13':0, 'x14':0, 'x15':0, 'x16':0, 'x17':0,
         'x18':0, 'x19':0, 'x20':0, 'x21':1, 'x22':0, 'x23':0, 
         'x24':1, 'x25':0, 'x26':0}

sym9 = Cascade(lines, sorted(lines.keys())[9:])
sym9.append(Toffoli(['x0'], 'x9'))
sym9.append(Toffoli(['x0', 'x8'], 'x9'))
sym9.append(Toffoli(['x8'], 'x9'))
sym9.append(Toffoli(['x7'], 'x10'))
sym9.append(Toffoli(['x7', 'x9'], 'x10'))
sym9.append(Toffoli(['x9'], 'x10'))
sym9.append(Toffoli(['x0', 'x8'], 'x11'))
sym9.append(Toffoli(['x11'], 'x12'))
sym9.append(Toffoli(['x7', 'x9'], 'x12'))
sym9.append(Toffoli(['x7', 'x11'], 'x12'))
sym9.append(Toffoli(['x12'], 'x13'))
sym9.append(Toffoli(['x1', 'x10'], 'x13'))
sym9.append(Toffoli(['x1', 'x12'], 'x13'))
sym9.append(Toffoli(['x7', 'x11'], 'x14'))
sym9.append(Toffoli(['x14'], 'x15'))
sym9.append(Toffoli(['x1', 'x12'], 'x15'))
sym9.append(Toffoli(['x1', 'x14'], 'x15'))
sym9.append(Toffoli(['x15'], 'x16'))
sym9.append(Toffoli(['x6', 'x13'], 'x16'))
sym9.append(Toffoli(['x6', 'x15'], 'x16'))
sym9.append(Toffoli(['x1', 'x14'], 'x17'))
sym9.append(Toffoli(['x17'], 'x18'))
sym9.append(Toffoli(['x6', 'x15'], 'x18'))
sym9.append(Toffoli(['x6', 'x17'], 'x18'))
sym9.append(Toffoli(['x18'], 'x19'))
sym9.append(Toffoli(['x2', 'x16'], 'x19'))
sym9.append(Toffoli(['x2', 'x18'], 'x19'))
sym9.append(Toffoli(['x1'], 'x20'))
sym9.append(Toffoli(['x1', 'x10'], 'x20'))
sym9.append(Toffoli(['x10'], 'x20'))
sym9.append(Toffoli(['x6'], 'x21'))
sym9.append(Toffoli(['x20'], 'x21'))
sym9.append(Toffoli(['x6', 'x17'], 'x21'))
sym9.append(Toffoli(['x6', 'x20'], 'x21'))
sym9.append(Toffoli(['x21'], 'x22'))
sym9.append(Toffoli(['x2', 'x18'], 'x22'))
sym9.append(Toffoli(['x2', 'x21'], 'x22'))
sym9.append(Toffoli(['x22'], 'x23'))
sym9.append(Toffoli(['x5', 'x19'], 'x23'))
sym9.append(Toffoli(['x5', 'x22'], 'x23'))
sym9.append(Toffoli(['x13'], 'x20'))
sym9.append(Toffoli(['x6', 'x20'], 'x13'))
sym9.append(Toffoli(['x2'], 'x24'))
sym9.append(Toffoli(['x13'], 'x24'))
sym9.append(Toffoli(['x2', 'x21'], 'x24'))
sym9.append(Toffoli(['x2', 'x13'], 'x24'))
sym9.append(Toffoli(['x24'], 'x25'))
sym9.append(Toffoli(['x5', 'x22'], 'x25'))
sym9.append(Toffoli(['x5', 'x24'], 'x25'))
sym9.append(Toffoli(['x25'], 'x26'))
sym9.append(Toffoli(['x4', 'x23'], 'x26'))
sym9.append(Toffoli(['x4', 'x25'], 'x26'))
sym9.append(Toffoli(['x16'], 'x13'))
sym9.append(Toffoli(['x2', 'x13'], 'x16'))
sym9.append(Inverter('x16'))
sym9.append(Toffoli(['x5', 'x16'], 'x24'))
sym9.append(Toffoli(['x5', 'x24'], 'x16'))
sym9.append(Toffoli(['x16'], 'x25'))
sym9.append(Toffoli(['x4', 'x25'], 'x16'))
sym9.append(Toffoli(['x16'], 'x26'))
sym9.append(Toffoli(['x3', 'x26'], 'x16'))
sym9.append(Inverter('x16'))


print "Original quantum cost:", sym9.cost()
print "Original gate count:", len(sym9)

ga = SmartGA(sym9, ['x16'])
ga.init_population_size = 500
ga.max_generations = 50000
ga.max_population_size = 50
ga.threshold = 1.0
ga.run()

print "Quantum Improvement:", (sym9.cost() - ga.bestgate.cost())
print "gate count Improvement:", ( len(sym9) - len(ga.bestgate))


