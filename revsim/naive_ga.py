# Revsim experimental
# Naive Genetic Algorithm with Limited Crossover
# Chris Rabl

import random

class NaiveGA:
    def __init__(self, spec):
        self.current_threshold = 1
        self.min_threshold = 0.01

        self.current_generations = 0
        self.max_generations = 1000

        self.current_population = 10
        self.max_population = 100

        self.individuals = []
        self.lines = {}

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

    def select_fitness(self):
        pass


def main():
    init_lines = []

    # Generate the initial population
    for i in range(0, current_population):
        c = Cascade.random(lines)
        individuals.append(c)

    while (current_threshold > min_threshold) and (current_generations > max_generations):
        individuals = select_fitness(individuals)
