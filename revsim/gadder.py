from revsim import *

lines = {'a':0, 'b':0, 'c':0, 's':0}
ideal = Cascade(lines, ['c', 's'])
ideal.append(Toffoli(['a', 'b'], 'c'))
ideal.append(Toffoli(['a'], 's'))
ideal.append(Toffoli(['b'], 's'))

# Generate the initial population                                                                                                          
ga = NaiveGA(ideal, ['c', 's'])
ga.threshold = 1.0
ga.init_population_size = 100
ga.max_generations = 20000
ga.max_gatecount_deviation = 4
ga.max_population_size = 3
ga.run()
