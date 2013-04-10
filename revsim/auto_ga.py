from revsim import *
import sys

r = RealReader(sys.argv[1])
ideal, non_garbage = r.read_cascade()
print "Original quantum cost:", ideal.cost()
print "Original gate count:", len(ideal)

ga = SmartGA(ideal, non_garbage)
ga.init_population_size = 50
ga.max_generations = 5000
ga.max_population_size = 50
ga.threshold = 1.0
ga.initial_population_mutations = 5
ga.subsequent_population_mutations = 2
ga.cost_improvement_goal = int(0.1 * ideal.cost()) # We want to reduce q cost by at least 10%
ga.max_removals_per_mutation = 2
ga.run()
print "Quantum Cost Improvement:", (ideal.cost() - ga.bestgate.cost())
print "Gate Count Improvement:", ( len(ideal) - len(ga.bestgate))

