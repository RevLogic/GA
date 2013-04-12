from revsim import *
import sys

r = RealReader(sys.argv[1])
ipop = int(sys.argv[2])
imut = int(sys.argv[3])
smut = int(sys.argv[4])
ctig = float(sys.argv[5])/100.0
mrpm = int(sys.argv[6])
ideal, non_garbage = r.read_cascade()
print "Original quantum cost:", ideal.cost()
print "Original gate count:", len(ideal)

ga = SmartGA(ideal, non_garbage)
ga.init_population_size = ipop # (50 - 500)
ga.max_generations = 5000
ga.max_population_size = ipop # (same as ipop)
ga.threshold = 1.0
ga.initial_population_mutations = imut # (5 - 10)
ga.subsequent_population_mutations = smut# (2 - 5)
ga.cost_improvement_goal = int( (ctig/100.0) * ideal.cost()) # We want to reduce q cost by at least ctig%
ga.max_removals_per_mutation = mrpm # (1-10)
ga.run()
print "Quantum Cost Improvement:", (ideal.cost() - ga.bestgate.cost())
print "Gate Count Improvement:", ( len(ideal) - len(ga.bestgate))

