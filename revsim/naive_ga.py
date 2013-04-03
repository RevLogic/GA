# Revsim experimental
# Naive Genetic Algorithm with Limited Crossover
# Chris Rabl

import random

class NaiveGA:
    def __init__(self, spec):
        self.threshold = 0.9

        self.max_generations = 1000

        self.population = []
        self.spec_length = len(spec)
        self.lines = spec.lines

        self.goal = TruthTable(spec)
        pass
    

    def crossover(self, parent_a, parent_b):
        children = []
        # Need to append because otherwise we refer to the same Cascade instance!!!
        children.append(Cascade(self.lines))
        children.append(Cascade(self.lines))
        children.append(Cascade(self.lines))
        children.append(Cascade(self.lines))

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
        d = c.copy()
        i = len(d)-1
        index = random.randint(0, i)
        d.remove(index)
        if index == i:
            d.append(random_toffoli(self.lines))
        else:
            d.insert(random_toffoli(self.lines), index)
        return d


    def random_toffoli(self):
        index_pool = self.lines.keys()
        width = len(index_pool)
        random.shuffle(index_pool)
        
        max_index = random.randint(1, width-1)
        control_list = index_pool[0:max_index]
        target = index_pool[max_index]
        
        return Toffoli(control_list, target)


    def fitness(c, goal, columns):
        return c.fuzzy_compare_columns(goal, columns)


    def run(self):
        current_fitness = 0.0
        gen_count = 0

        non_garbage_lines = ['c', 's']

        # Generate initial population
        
        while (current_fitness < self.threshold) and (gen_count < self.max_generations):
            tt = TruthTable(c)
            current_fitness = fitness(tt, spec, non_garbage_lines)
            d = mutate(c, new_lines)
            
            new_tt = TruthTable(d)
            new_fitness = fitness(new_tt, spec, non_garbage_lines)

            if new_fitness > current_fitness:
                print "Generation:",gen_count, "\t\tFitness:", current_fitness, "\t\tCost Decrease?", (d.cost < c.cost)
                c = d.copy()
            gen_count += 1


def main():
    lines = {'a':0, 'b':0, 'c':0, 's':0}
    ideal = Cascade(in_lines, ['c', 's'])
    ideal.append(Toffoli(['a', 'b'], 'c'))
    ideal.append(Toffoli(['a'], 's'))
    ideal.append(Toffoli(['b'], 's'))

    # Generate the initial population
    for i in range(0, current_population):
        c = Cascade.random(lines)
        individuals.append(c)

    ga.run()


if __name__ == "__main__":
    main()
