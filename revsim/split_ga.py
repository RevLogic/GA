# Revsim experimental

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# FOR INTERNAL TESTING ONLY: DO NOT DEPLOY ON CONDOR
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Description: Multiprocessing implementation of
# "splitting" Genetic Algorithm
# Author: Chris Rabl


from multiprocessing import Pool
import sys

from revsim import *

def smartGA_pool_runner(block):
    ga = SmartGA(block, block.lines) # Need to use all lines
    ga.eval_qcost = False
    ga.init_population_size = 100 # (50 - 500)
    ga.max_generations = 10000
    ga.max_population_size = 30 # (same as ipop)
    ga.threshold = 1.0
    ga.initial_population_mutations = 5 # (5 - 10)
    ga.subsequent_population_mutations = 2 # (2 - 5)
    ga.cost_improvement_goal = int( (5.0/100.0) * block.cost()) 
    ga.max_removals_per_mutation = 2 # (1-10)
    return ga.run()

def create_cascade(lines, gates):
    c = Cascade(lines)
    c.replace_gates(gates)
    return c

def split_ga(filename):
    # Start 2 worker processes: we use subprocesses to avoid GIL
    pool = Pool(processes=4)
    
    r = RealReader(filename)
    ideal, non_garbage = r.read_cascade()
    
    print "Original quantum cost:", ideal.cost()
    print "Original gate count:", len(ideal)
    
    def partition(l, n):
        for i in xrange(0, len(l), n):
            yield l[i:i+n]
            
    max_cascade_length = 20;

    # The most terrible list comprehension ever...
    cascade_list = [create_cascade(ideal.lines, gates) for gates in list(partition(ideal, max_cascade_length))]

    ideal_copy = ideal.copy()

    new_cascade_list = pool.map_async(smartGA_pool_runner, cascade_list).get(9999999) # this is an UGLY python hack

    final_cascade = Cascade(ideal.lines)

    print "-----------------------------------"
    print "Final Cascade: "

    for cascade in new_cascade_list:
        for gate in cascade:
            print gate
            final_cascade.append(gate)
            
    
    print "Quantum Cost Improvement:", ideal_copy.cost() - final_cascade.cost()
    print "Gate Count Improvement:", len(ideal_copy) - len(final_cascade)
    
if __name__ == "__main__":
    filename = sys.argv[1]
    split_ga(filename)
