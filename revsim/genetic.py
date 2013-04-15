# Revsim
# Genetic Algorithm Class
# For developing GAs that follow a given template with crossover
# and mutation

#this is a quick change

import random

from cascade import *
from truth_table import *

class GeneticAlgorithm:
    def __init__(self, spec, non_garbage_lines):
        """
        Perform initialization on all GA parameters. These may be set by accessing the
        member variables directly before calling GeneticAlgorithm.run(). The default values
        will almost certainly not work in the average case.
        """
        self.threshold = 0.9
        
        # Initial population parameters
        self.init_population_size = 500 # Number of initial population members 
        self.max_generations = 10000 # maximum number of generations that the GA should run
        self.max_gatecount_deviation = 2 # used in the naive GA when generating intial populations of random circuits: how many gates can the generated population members add to the length of the ideal cascade?
        self.cost_improvement_goal = 10 # number of gates by which the cascade should be reduced AT LEAST

        self.population = []
        self.max_population_size = 50 # maximum subsequent population size for every generation in our evolution

        self.initial_population_mutations = 15 # maximum number of mutations that we should perform on EACH CASCADE in our initial population
        self.subsequent_population_mutations = 3 # maximum number of mutations that we should perform on EACH CASCADE in subsequent populations
        self.max_removals_per_mutation = 2 # the maximum number of gates that we should remove if our mutation does gate removals. the larger this number, the more aggressive the optimization will be, however it may yield undesired results on large circuits (divergence comes to mind)
        
        self.parent = spec # Cascade that specifies the function that we wish to compute
        self.spec_length = len(spec)
        self.lines = spec.lines
        #self.lines = dict(zip(spec.variable_line_labels(), [0] * spec.logical_width()))
        #for line in non_garbage_lines:
        #    self.lines[line] = 0
        #
        self.constant_lines = spec.constant_line_labels()
        #self.constant_lines = non_garbage_lines

        self.goal = TruthTable(spec)
        self.non_garbage = non_garbage_lines
    

    def crossover(self, parent_a, parent_b):
        """
        Override this method in your own GA class. This method is designed to
        take two members of the Cascade population and cross them over in some way.
        """
        pass


    def mutate(self, c):
        """
        Override this method in your own GA class. This method is designed to
        perform mutation on a given Cascade in a population. For GAs that rely only
        on crossover, this method may be omitted.
        """
        pass


    def random_toffoli(self):
        """
        Generates a random Toffoli gate, given a set of available input lines.
        All line indices go into an "index pool", from which control and target
        values can be chosen. These gates are limited to 3 controls and 1 target.
        """
        index_pool = self.lines.keys()
        width = len(index_pool)
        random.shuffle(index_pool)
        
        #max_index = 2
        max_index = random.randint(1, min(4, width-1))
        control_list = index_pool[0:max_index]
        target = index_pool[max_index]
        
        return Toffoli(control_list, target)


    def fitness(self, c):
        """
        Prototype method for measuring the fitness of a given Cascade according to
        some metric (quantum cost, gate count, etc.)
        """
        pass


    def generate_population(self, pop_size):
        """
        Prototype method for generating initial and subsequent populations according
        to the "pop_size" parameter, which denotes how large the population should be.
        """
        pass
    

    def run(self):
        """
        Prototype method to run the Genetic Algorithm. This MUST be overridden by modules
        that subclass from GeneticAlgorithm.
        """
        pass
