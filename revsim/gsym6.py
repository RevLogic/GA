# Revsim experimental
# This is a VERY rough implementation of a basic mutation-only GA
# Crossover is not implemented, and the only thing we are trying to
# build is an adder, but it works!


from revsim import *

lines = {'x1':0,  'x2':0, 'x3':0, 'x4':0, 'x5':0, 
            'x6':0,  's2':0, 's3':0, 's4':0, 's5':0}

threshold = 0.9
sym6 = Cascade(lines, ['s2', 's3', 's4', 's5'])
sym6.append(Toffoli(['x1', 'x2'], 's2'))
sym6.append(Toffoli(['x1'], 'x2'))
sym6.append(Toffoli(['x3', 's2'], 's3'))
sym6.append(Toffoli(['x2', 'x3'], 's2'))
sym6.append(Toffoli(['x2'], 'x3'))
sym6.append(Toffoli(['x4', 's3'], 's4'))
sym6.append(Toffoli(['x4', 's2'], 's3'))
sym6.append(Toffoli(['x3', 'x4'], 's2'))
sym6.append(Toffoli(['x3'], 'x4'))
sym6.append(Toffoli(['x5', 's4'], 's5'))
sym6.append(Toffoli(['x5', 's3'], 's4'))
sym6.append(Toffoli(['x5', 's2'], 's3'))
sym6.append(Toffoli(['x4', 'x5'], 's2'))
sym6.append(Toffoli(['x4'], 'x5'))
sym6.append(Toffoli(['x6', 's4'], 's5'))
sym6.append(Toffoli(['x6', 's3'], 's4'))
sym6.append(Toffoli(['x5', 'x6'], 's2'))
sym6.append(Toffoli(['x5'], 'x6'))
sym6.append(Toffoli(['s2'], 's5'))
sym6.append(Toffoli(['s4'], 's5'))

print "Initial Quantum Cost:", sym6.cost()
print "Initial Gate Count:", len(sym6)

ga = SmartGA(sym6, ['s5'])
ga.init_population_size = 500
ga.max_generations = 50000
ga.max_gatecount_deviation = 20
ga.max_population_size = 35
ga.threshold = 1.0
ga.run()
print "Quantum Improvement:", (sym6.cost() - ga.bestgate.cost())  
print "gate count Improvement:", ( len(sym6) - len(ga.bestgate))
