from revsim import *

lines = {'a':0, 'b':0, 'c':0, 's':0}
ideal = Cascade(lines, ['c', 's'])
ideal.append(Toffoli(['a', 'b'], 'c'))
ideal.append(Toffoli(['a'], 's'))
ideal.append(Toffoli(['b'], 's'))

# Generate the initial population                                                                                                          
ga = NaiveGA(ideal, ['c', 's'])

ga.init_population_size = 500
ga.max_generations = 10000
ga.max_gatecount_deviation = 2
ga.max_population_size = 50

ga.run()
