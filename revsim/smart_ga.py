# Revsim 
# "Smart genetic algorithm" that utilizes the original circuit spec as a seed

import os
from genetic import *

class SmartGA(GeneticAlgorithm):
    def crossover(self, parent_a, parent_b):
        children = []
        
        children.append(Cascade(self.lines, self.constant_lines))
        children.append(Cascade(self.lines, self.constant_lines))

        # Construct first child. Half of A, half of B 
        for gate in parent_a[0:len(parent_a)/2]:
            children[0].append(gate)
        for gate in parent_b[len(parent_b)/2:len(parent_b)]:
            children[0].append(gate)

        # Construct second child. Half of B, half of A
        for gate in parent_b[0:len(parent_b)/2]:
            children[1].append(gate)
        for gate in parent_a[len(parent_a)/2:len(parent_a)]:
            children[1].append(gate)

        return children


    def generate_population(self, pop_size, num_mutations=0):
        """
        Generates an initial population based on a seed Cascade
        """
        self.population = []
        for i in xrange(0, pop_size):
            member = self.parent.copy()
            for j in xrange(0, num_mutations):
                self.mutate(member)
            self.population.append(member)
            

    def mutate(self, c):
        """
        Either remove a gate at random or replace it with a random gate
        """
        choice = random.randint(0,3)

        if (choice == 0 or choice == 1) and len(c) > 1:
            for i in range(0, self.max_removals_per_mutation):
                try:
                    c.remove(random.randint(0, len(c)-1)) # Randomly remove a gate
                except ValueError:
                    print "ERROR: trying to remove more gates than there are in the Cascade"
                    print "You should try decreasing the GA's self.max_removals_per_mutation parameter"
                    exit()
        elif choice == 2:
            c.append(self.random_toffoli())
        else:
            # or replace a gate with a random gate
            i = len(c)-1
            index = random.randint(0, i)
            c.remove(index)
            if index == i:
                c.append(self.random_toffoli())
            else:
                c.insert(self.random_toffoli(), index)
    
                
    def fitness(self, truth_table, quantum_cost_goal):
        function_eval = truth_table.fuzzy_compare_columns(self.goal, self.non_garbage)
        qcost_fitness = min(quantum_cost_goal / truth_table.c.cost(), 1.0)
        
        return function_eval # * qcost_fitness

    
    def run(self):
        quantum_cost_goal = self.parent.cost() - self.cost_improvement_goal
        """
        print "Smart GA Parameters"
        print "Initial Population Count:", self.init_population_size
        print "Initial Population Mutations:", self.initial_population_mutations
        print "Subsequent Population Count:", self.max_population_size
        print "Subsequent Population Mutations:", self.subsequent_population_mutations
        print "Maximum Number of Generations:", self.max_generations
        print "Quantum Cost Goal:", quantum_cost_goal
        print ""
        """

        print "Starting Revsim SmartGA... PID", os.getpid()
        pidstring = "[SGA "+str(os.getpid())+"]"
        current_fitness = 0.0
        gen_count = 0

        non_garbage_lines = self.non_garbage
        # Generate initial population 
        self.generate_population(self.init_population_size, self.initial_population_mutations)

        while (current_fitness < self.threshold) and (gen_count < self.max_generations):
            mutate_index = random.randint(0, len(self.population)-1)
            self.mutate(self.population[mutate_index])

            fits = [(self.fitness(TruthTable(c), quantum_cost_goal), c) for c in self.population]
            fits.sort()
            top_two = fits[-2:]
            
            new_cost = top_two[1][1].cost()
            new_fitness = top_two[1][0]

            random_two = []
            random_two.append(fits[random.randint(0, len(fits)-3)][1])
            random_two.append(fits[random.randint(0, len(fits)-3)][1])

            if new_fitness > current_fitness:
                print pidstring, "Generation:",gen_count, "\t\tFitness:", new_fitness
                #self.population += self.crossover(self.parent, top_two[0][1])
                #self.population += self.crossover(self.parent, top_two[1][1])
                self.population += self.crossover(top_two[0][1], top_two[1][1])

                # Add randomly chosen ones to the mix
                self.population += self.crossover(random_two[0], random_two[1])
                self.population += self.crossover(top_two[0][1], random_two[0])
                self.population += self.crossover(top_two[0][1], random_two[1])
                self.population += self.crossover(top_two[1][1], random_two[0])
                self.population += self.crossover(top_two[1][1], random_two[1])
                #self.population += self.crossover(self.parent, random_two[0])
                #self.population += self.crossover(self.parent, random_two[1])

                current_fitness = new_fitness
            else:
                self.generate_population(self.max_population_size, self.subsequent_population_mutations)
                self.population += [top_two[0][1], top_two[1][1]]

            if (gen_count == self.max_generations - 1) or (current_fitness == 1.0):
                if gen_count == self.max_generations - 1:
                    print pidstring, "GENERATION LIMIT EXCEEDED!"
                    print pidstring, "Fitness:", current_fitness
                    if current_fitness != 1:
                        return self.parent
                best = top_two[1][1]
                self.bestgate = best
                    
                print pidstring, "Quantum Cost:", best.cost()
                print pidstring, "Gate Count:", len(best)
                return best

            gen_count += 1
