from revsim import *
import sys

def ga_runner(filename, optimization_factor):
    r = RealReader(filename)
    ideal, non_garbage = r.read_cascade()
    print "Original quantum cost:", ideal.cost()
    print "Original gate count:", len(ideal)
    
    ga = SmartGA(ideal, non_garbage)
    ga.init_population_size = 100 # (50 - 500)
    ga.max_generations = 50000
    ga.max_population_size = 20 # (same as ipop)
    ga.threshold = 1.0
    ga.initial_population_mutations = 5 # (5 - 10)
    ga.subsequent_population_mutations = 2 # (2 - 5)
    ga.cost_improvement_goal = int( (optimization_factor/100.0) * ideal.cost()) # We want to reduce q cost by at least ctig%
    ga.max_removals_per_mutation = 2 # (1-10)
    r = ga.run()
    print "Quantum Cost Improvement:", (ideal.cost() - ga.bestgate.cost())
    print "Gate Count Improvement:", ( len(ideal) - len(ga.bestgate))
    return r

if __name__ == "__main__":
    filename = sys.argv[1]
    ga_runner(filename, 10)
