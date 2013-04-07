from revsim import *
import sys

ideal, non_garbage = parser.parse(sys.argv[1])
print "Original quantum cost:", ideal.cost()
print "Original gate count:", len(ideal)

ga = SmartGA(ideal, non_garbage)
ga.init_population_size = 50
ga.max_generations = 1000
ga.max_population_size = 50
ga.threshold = 1.0
ga.initial_population_mutations = 20
ga.subsequent_population_mutations = 5
ga.run()
print "Quantum Cost Improvement:", (ideal.cost() - ga.bestgate.cost())
print "Gate Count Improvement:", ( len(ideal) - len(ga.bestgate))

