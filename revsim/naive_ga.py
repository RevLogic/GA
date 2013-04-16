# Revsim experimental
# Naive Genetic Algorithm with Limited Crossover
# Chris Rabl

from genetic import *

class NaiveGA(GeneticAlgorithm):
    def crossover(self, parent_a, parent_b):
        children = []
        # Need to append because otherwise we refer to the same Cascade instance!!!
        children.append(Cascade(self.lines, self.constant_lines))
        children.append(Cascade(self.lines, self.constant_lines))
        children.append(Cascade(self.lines, self.constant_lines))
        children.append(Cascade(self.lines, self.constant_lines))

        # TODO: Are there better ways to do crossover?

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

        # Select even index gates from A, odd index gates from B
        for gate in parent_a[0::2]:
            children[2].append(gate)
        for gate in parent_b[1::2]:
            children[2].append(gate)

        # Select odd index gates from A, even index gates from B
        for gate in parent_b[0::2]:
            children[3].append(gate)
        for gate in parent_a[1::2]:
            children[3].append(gate)
        
        return children


    def generate_population(self, pop_size):
        self.population = []
        for i in xrange(0, pop_size):
            c_length = random.randint(2, self.spec_length+self.max_gatecount_deviation)
            self.population.append(Cascade(self.lines, self.constant_lines))
            for j in xrange(1, c_length):
                self.population[i].append(self.random_toffoli())


    def mutate(self, c):
        i = len(c)-1
        index = random.randint(0, i)
        c.remove(index)
        if index == i:
            c.append(self.random_toffoli())
        else:
            c.insert(self.random_toffoli(), index)


    def fitness(self, c):
        return c.fuzzy_compare_columns(self.goal, self.non_garbage)

    
    def run(self):
        print "Naive GA Parameters"
        print "Initial Population Count:", self.init_population_size
        print "Subsequent Population Count:", self.max_population_size
        print "Maximum Number of Generations:", self.max_generations
        print "Maximum Gate Count Deviation:", self.max_gatecount_deviation
        print ""
        
        current_fitness = 0.0
        gen_count = 0

        non_garbage_lines = self.non_garbage
        # Generate initial population
        self.generate_population(self.init_population_size)
        
        while (current_fitness < self.threshold) and (gen_count < self.max_generations):
            mutate_index = random.randint(0, len(self.population)-1)
            self.mutate(self.population[mutate_index])
    
            fits = [(self.fitness(TruthTable(c)), c) for c in self.population]
            fits.sort()
            top_two = fits[-2:]

            new_fitness = top_two[1][0]

            if new_fitness > current_fitness:
                print "Generation:",gen_count, "\t\tFitness:", new_fitness
                self.population += self.crossover(self.parent, top_two[0][1])
                self.population += self.crossover(self.parent, top_two[1][1])
                self.population += self.crossover(top_two[0][1], top_two[1][1])
                current_fitness = new_fitness
            else:
                self.generate_population(self.max_population_size)
                self.population += [top_two[0][1], top_two[1][1]]
        
            if (gen_count == self.max_generations - 1) or (current_fitness == 1.0):
                best = top_two[1][1]
                for gate in best:
                    print gate
                print "Quantum Cost:", best.cost()
                print "Gate Count:", len(best)

                return best
            gen_count += 1
