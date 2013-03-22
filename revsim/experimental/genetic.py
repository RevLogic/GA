class GeneticAlgorithm:
    def __init__(self, cascade):
        self.current_threshold = 1
        self.min_threshold = 0.01

        self.current_generations = 0
        self.max_generations = 1000

        self.current_population = 10
        self.max_population = 100

        self.individuals = []
        self.lines = {}

        pass
    
    def crossover(self, parent_a, parent_b):
        child_a = Cascade(self.lines)
        child_b = Cascade(self.lines)
        
        # Construct first child. Half of A, half of B
        for gate in parent_a[0:len(parent_a)/2]:
            child_a.append(gate)
        for gate in parent_b[len(parent_b)/2:len(parent_b)]:
            child_a.append(gate)
        
        # Construct second child. Half of B, half of A
        for gate in parent_b[0:len(parent_b)/2]:
            child_b.append(gate)
        for gate in parent_a[len(parent_a)/2:len(parent_a)]:
            child_b.append(gate)
        
        return child_a, child_b

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
