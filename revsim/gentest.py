# Revsim experimental
# This is a VERY rough implementation of a basic mutation-only GA
# Crossover is not implemented, and the only thing we are trying to
# build is an adder, but it works!


from revsim import *
import random


in_lines = {'a':0, 'b':0, 'c':0, 's':0}
ideal = Cascade(in_lines, ['c', 's'])
ideal.append(Toffoli(['a', 'b'], 'c'))
ideal.append(Toffoli(['a'], 's'))
ideal.append(Toffoli(['b'], 's'))

spec = TruthTable(ideal)

def random_toffoli(lines):
    index_pool = lines.keys()
    width = len(index_pool)
    random.shuffle(index_pool)

    max_index = random.randint(1, width-1)
    control_list = index_pool[0:max_index]
    target = index_pool[max_index]
    
    return Toffoli(control_list, target)


def mutate(c, lines):
    d = c.copy()
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

    
c = Cascade(in_lines, ['c', 's'])
for i in range(0, 4):
    c.append(random_toffoli(in_lines))


current_fitness = 0.0
threshold = 0.9

gen_count = 0
max_generations = 1000

while (current_fitness < threshold) and (gen_count < max_generations):
    tt = TruthTable(c)
    current_fitness = fitness(tt, spec, c.constant_line_labels())
    d = mutate(c, in_lines)
    new_tt = TruthTable(d)
    new_fitness = fitness(new_tt, spec, d.constant_line_labels())

    if new_fitness > current_fitness:
        c = d.copy()

    gen_count += 1

tt = TruthTable(c)
print "Found a cascade with fitness:", fitness(tt, spec, c.constant_line_labels())
print "After", gen_count, "generations"
print "Whose circuit spec is:"

for gate in c:
    print gate

print ""
print "And whose truth table is:"
print tt
