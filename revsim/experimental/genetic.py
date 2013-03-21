class GeneticAlgorithm:
    current_threshold = 1
    min_threshold = 0.01

    current_generations = 0
    max_generations = 1000

    current_population = 10
    max_population = 100

    individuals = []


    def __init__(self, cascade):
        pass
    
    def crossover(self, parent1, parent2):
        pass

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
