# Revsim experimental
# This is a VERY rough implementation of a basic mutation-only GA
# Crossover is not implemented, and the only thing we are trying to
# build is an adder, but it works!


from revsim import *

lines = {'x1':0,  'x2':0, 'x3':0, 'x4':0, 'x5':0, 
            'x6':0,  's2':0, 's3':0, 's4':0, 's5':0}

threshold = 0.9
ideal = Cascade(lines, ['s2', 's3', 's4', 's5'])
ideal.append(Toffoli(['x1', 'x2'], 's2'))
ideal.append(Toffoli(['x1'], 'x2'))
ideal.append(Toffoli(['x3', 's2'], 's3'))
ideal.append(Toffoli(['x2', 'x3'], 's2'))
ideal.append(Toffoli(['x2'], 'x3'))
ideal.append(Toffoli(['x4', 's3'], 's4'))
ideal.append(Toffoli(['x4', 's2'], 's3'))
ideal.append(Toffoli(['x3', 'x4'], 's2'))
ideal.append(Toffoli(['x3'], 'x4'))
ideal.append(Toffoli(['x5', 's4'], 's5'))
ideal.append(Toffoli(['x5', 's3'], 's4'))
ideal.append(Toffoli(['x5', 's2'], 's3'))
ideal.append(Toffoli(['x4', 'x5'], 's2'))
ideal.append(Toffoli(['x4'], 'x5'))
ideal.append(Toffoli(['x6', 's4'], 's5'))
ideal.append(Toffoli(['x6', 's3'], 's4'))
ideal.append(Toffoli(['x5', 'x6'], 's2'))
ideal.append(Toffoli(['x5'], 'x6'))
ideal.append(Toffoli(['s2'], 's5'))
ideal.append(Toffoli(['s4'], 's5'))

ga = NaiveGA(ideal, ['s5'])
ga.init_population_size = 1000
ga.max_generations = 10000
ga.max_gatecount_deviation = 20
ga.max_population_size = 20
ga.run()
