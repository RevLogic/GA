# Revsim experimental
# This is a VERY rough implementation of a basic mutation-only GA
# Crossover is not implemented, and the only thing we are trying to
# build is an adder, but it works!


from revsim import *
import random
import sys

max_generations = int(sys.argv[1])
max_cascade_length = int(sys.argv[2])


in_lines = {'x1':0,  'x2':0, 'x3':0, 'x4':0, 'x5':0, 
            'x6':0,  's2':0, 's3':0, 's4':0, 's5':0}

ideal = Cascade(in_lines, ['s2', 's3', 's4', 's5'])
ideal.append(Toffoli(['x1', 'x2'], 's2'))
ideal.append(Toffoli(['x1'], 'x2'))
ideal.append(Toffoli(['x3', 's2'], 's3'))
ideal.append(Toffoli(['x2', 'x3'], 's2'))
ideal.append(Toffoli(['x2'], 'x3'))
ideal.append(Toffoli(['x4', 's3'], 's4'))
ideal.append(Toffoli(['x4', 's2'], 's3'))
ideal.append(Toffoli(['x3', 'x4'], 's2'))
ideal.append(Toffoli(['x3'], 'x4'))
ideal.append(Toffoli(['x5', 's4'], 's5'))
ideal.append(Toffoli(['x5', 's3'], 's4'))
ideal.append(Toffoli(['x5', 's2'], 's3'))
ideal.append(Toffoli(['x4', 'x5'], 's2'))
ideal.append(Toffoli(['x4'], 'x5'))
ideal.append(Toffoli(['x6', 's4'], 's5'))
ideal.append(Toffoli(['x6', 's3'], 's4'))
ideal.append(Toffoli(['x5', 'x6'], 's2'))
ideal.append(Toffoli(['x5'], 'x6'))
ideal.append(Toffoli(['s2'], 's5'))
ideal.append(Toffoli(['s4'], 's5'))

spec = TruthTable(ideal)

def random_toffoli(lines):
    index_pool = lines.keys()
    width = len(index_pool)
    random.shuffle(index_pool)

    # Experiment to see if "smaller" toffoli gates are better
    max_index = random.randint(1, min(4, width-1)) 
    control_list = index_pool[0:max_index]
    target = index_pool[max_index]
    #target = 's5' # test to see if we use only one target

    return Toffoli(control_list, target)


def mutate(c, lines):
    d = c.copy()
    
    choice = random.randint(1,5)

    if choice == 1:
        d.remove(random.randint(0,len(d)-1))
    elif choice == 2:
        d.append(random_toffoli(lines))
        pass
    else:
        i = len(d)-1
        index = random.randint(0, i)
        d.remove(index)
        if index == i:
            d.append(random_toffoli(lines))
        else:
            d.insert(random_toffoli(lines), index)

    return d


def crossover(p1, p2):
    pass


def fitness(c, goal, columns):
    return c.fuzzy_compare_columns(goal, columns)

new_lines = {'x0':0, 'x1':0, 'x2':0, 'x3':0, 'x4':0, 'x5':0, 's5':0}
c = Cascade(new_lines, ['s5'])
for i in range(0, max_cascade_length):
    c.append(random_toffoli(new_lines))


current_fitness = 0.0
threshold = 1.0

gen_count = 0
non_garbage_lines = ['s5']

while (current_fitness < threshold) and (gen_count < max_generations):
    tt = TruthTable(c)
    current_fitness = fitness(tt, spec, non_garbage_lines)
    d = mutate(c, new_lines)
    #d = mutate(d, new_lines)
    #d = mutate(d, new_lines)
    new_tt = TruthTable(d)
    new_fitness = fitness(new_tt, spec, non_garbage_lines)

    if new_fitness > current_fitness:
        print "Generation:",gen_count, "\t\tFitness:", current_fitness, "\t\tCost Decrease?", (d.cost < c.cost)
        c = d.copy()
    gen_count += 1

tt = TruthTable(c)
print "Found a cascade with fitness:", fitness(tt, spec, non_garbage_lines)
print "After", gen_count, "generations"
print "Whose circuit spec is:"

for gate in c:
    print gate

print "Gate count:", len(c)
print "Quantum cost:", c.cost()
