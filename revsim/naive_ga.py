# Revsim experimental
# Naive Genetic Algorithm with Limited Crossover
# Chris Rabl

from revsim import *
import random

class NaiveGA:
    def __init__(self, spec, non_garbage_lines):
        self.threshold = 0.9

        self.init_population_size = 10000
        self.max_generations = 20000
        self.max_gatecount_deviation = 10

        self.population = []
        self.spec_length = len(spec)
        self.lines = spec.lines
        self.constant_lines = spec.constant_line_labels()
        
        self.goal = TruthTable(spec)
        self.non_garbage = non_garbage_lines
    

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


    def mutate(self, c):
        i = len(c)-1
        index = random.randint(0, i)
        c.remove(index)
        if index == i:
            c.append(self.random_toffoli())
        else:
            c.insert(self.random_toffoli(), index)


    def random_toffoli(self):
        index_pool = self.lines.keys()
        width = len(index_pool)
        random.shuffle(index_pool)
        
        max_index = random.randint(1, width-1)
        control_list = index_pool[0:max_index]
        target = index_pool[max_index]
        
        return Toffoli(control_list, target)


    def fitness(self, c):
        return c.fuzzy_compare_columns(self.goal, self.non_garbage)


    def run(self):
        current_fitness = 0.0
        gen_count = 0

        non_garbage_lines = self.non_garbage
        # Generate initial population
        for i in xrange(0, self.init_population_size):
            c_length = random.randint(2, self.spec_length+self.max_gatecount_deviation)
            self.population.append(Cascade(self.lines, self.constant_lines))
            for j in xrange(1, c_length):
                self.population[i].append(self.random_toffoli())
        
        while (current_fitness < self.threshold) and (gen_count < self.max_generations):
            mutate_index = random.randint(0, len(self.population)-1)
            self.mutate(self.population[mutate_index])
    
            fits = [(self.fitness(TruthTable(c)), c) for c in self.population]
            fits.sort()
            top_two = fits[-2:]
            new_fitness = top_two[1][0]

            if new_fitness > current_fitness:
                print "Generation:",gen_count, "\t\tFitness:", new_fitness
                self.population = self.crossover(top_two[0][1], top_two[1][1])
                current_fitness = new_fitness
        
            if (gen_count == self.max_generations - 1) or (current_fitness == 1.0):
                best = top_two[1][1]
                for gate in best:
                    print gate
                print "Quantum Cost:", best.cost()
                print "Gate Count:", len(best)
            gen_count += 1

        


def main():
    lines = {'a':0, 'b':0, 'c':0, 's':0}
    ideal = Cascade(lines, ['c', 's'])
    ideal.append(Toffoli(['a', 'b'], 'c'))
    ideal.append(Toffoli(['a'], 's'))
    ideal.append(Toffoli(['b'], 's'))

    # Generate the initial population
    ga = NaiveGA(ideal, ['c', 's'])
    ga.run()


if __name__ == "__main__":
    main()
