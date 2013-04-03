# Revsim experimental
# This is a VERY rough implementation of a basic mutation-only GA
# Crossover is not implemented, and the only thing we are trying to
# build is an adder, but it works!


from revsim import *
import random


in_lines = {'x0':0,  'x1':0,  'x2':0,  'x3':0, 'x4':0,   'x5':0, 
         'x6':0,  'x7':0,  'x8':0,  'x9':0, 'x10': 0, 'x11':0,
         'x12':0, 'x13':0, 'x14':0, 'x15':0, 'x16':0, 'x17':0,
         'x18':0, 'x19':0, 'x20':0, 'x21':1, 'x22':0, 'x23':0, 
         'x24':1, 'x25':0, 'x26':0}

ideal = Cascade(in_lines, sorted(in_lines.keys())[9:])
"""

    c.append(Toffoli(['d','e'], 'f'))
    c.append(Toffoli(['f','g'], 'j'))
    c.append(Toffoli(['b','c','d','e','f'], 'g'))
    c.append(Toffoli(['a','c','e','g','i'], 'j'))

"""

ideal.append(Toffoli(['x0'], 'x9'))
ideal.append(Toffoli(['x0', 'x8'], 'x9'))
ideal.append(Toffoli(['x8'], 'x9'))
ideal.append(Toffoli(['x7'], 'x10'))
ideal.append(Toffoli(['x7', 'x9'], 'x10'))
ideal.append(Toffoli(['x9'], 'x10'))
ideal.append(Toffoli(['x0', 'x8'], 'x11'))
ideal.append(Toffoli(['x11'], 'x12'))
ideal.append(Toffoli(['x7', 'x9'], 'x12'))
ideal.append(Toffoli(['x7', 'x11'], 'x12'))
ideal.append(Toffoli(['x12'], 'x13'))
ideal.append(Toffoli(['x1', 'x10'], 'x13'))
ideal.append(Toffoli(['x1', 'x12'], 'x13'))
ideal.append(Toffoli(['x7', 'x11'], 'x14'))
ideal.append(Toffoli(['x14'], 'x15'))
ideal.append(Toffoli(['x1', 'x12'], 'x15'))
ideal.append(Toffoli(['x1', 'x14'], 'x15'))
ideal.append(Toffoli(['x15'], 'x16'))
ideal.append(Toffoli(['x6', 'x13'], 'x16'))
ideal.append(Toffoli(['x6', 'x15'], 'x16'))
ideal.append(Toffoli(['x1', 'x14'], 'x17'))
ideal.append(Toffoli(['x17'], 'x18'))
ideal.append(Toffoli(['x6', 'x15'], 'x18'))
ideal.append(Toffoli(['x6', 'x17'], 'x18'))
ideal.append(Toffoli(['x18'], 'x19'))
ideal.append(Toffoli(['x2', 'x16'], 'x19'))
ideal.append(Toffoli(['x2', 'x18'], 'x19'))
ideal.append(Toffoli(['x1'], 'x20'))
ideal.append(Toffoli(['x1', 'x10'], 'x20'))
ideal.append(Toffoli(['x10'], 'x20'))
ideal.append(Toffoli(['x6'], 'x21'))
ideal.append(Toffoli(['x20'], 'x21'))
ideal.append(Toffoli(['x6', 'x17'], 'x21'))
ideal.append(Toffoli(['x6', 'x20'], 'x21'))
ideal.append(Toffoli(['x21'], 'x22'))
ideal.append(Toffoli(['x2', 'x18'], 'x22'))
ideal.append(Toffoli(['x2', 'x21'], 'x22'))
ideal.append(Toffoli(['x22'], 'x23'))
ideal.append(Toffoli(['x5', 'x19'], 'x23'))
ideal.append(Toffoli(['x5', 'x22'], 'x23'))
ideal.append(Toffoli(['x13'], 'x20'))
ideal.append(Toffoli(['x6', 'x20'], 'x13'))
ideal.append(Toffoli(['x2'], 'x24'))
ideal.append(Toffoli(['x13'], 'x24'))
ideal.append(Toffoli(['x2', 'x21'], 'x24'))
ideal.append(Toffoli(['x2', 'x13'], 'x24'))
ideal.append(Toffoli(['x24'], 'x25'))
ideal.append(Toffoli(['x5', 'x22'], 'x25'))
ideal.append(Toffoli(['x5', 'x24'], 'x25'))
ideal.append(Toffoli(['x25'], 'x26'))
ideal.append(Toffoli(['x4', 'x23'], 'x26'))
ideal.append(Toffoli(['x4', 'x25'], 'x26'))
ideal.append(Toffoli(['x16'], 'x13'))
ideal.append(Toffoli(['x2', 'x13'], 'x16'))
ideal.append(Inverter('x16'))
ideal.append(Toffoli(['x5', 'x16'], 'x24'))
ideal.append(Toffoli(['x5', 'x24'], 'x16'))
ideal.append(Toffoli(['x16'], 'x25'))
ideal.append(Toffoli(['x4', 'x25'], 'x16'))
ideal.append(Toffoli(['x16'], 'x26'))
ideal.append(Toffoli(['x3', 'x26'], 'x16'))
ideal.append(Inverter('x16'))

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

new_lines = {'x0':0, 'x1':0, 'x2':0, 'x3':0, 'x4':0, 'x5':0, 'x6':0, 'x7':0, 'x8':0, 'x16':0}
c = Cascade(new_lines, ['x16'])
for i in range(0, 20):
    c.append(random_toffoli(new_lines))


current_fitness = 0.0
threshold = 0.9

gen_count = 0
max_generations = 1000
non_garbage_lines = ['x16']

print ideal.logical_width()
print c.logical_width()

while (current_fitness < threshold) and (gen_count < max_generations):
    tt = TruthTable(c)
    current_fitness = fitness(tt, spec, non_garbage_lines)
    d = mutate(c, new_lines)
    new_tt = TruthTable(d)
    new_fitness = fitness(new_tt, spec, non_garbage_lines)

    if new_fitness > current_fitness:
        c = d.copy()

    print "Generation:",gen_count
    gen_count += 1

tt = TruthTable(c)
print "Found a cascade with fitness:", fitness(tt, spec, non_garbage_lines)
print "After", gen_count, "generations"
print "Whose circuit spec is:"

for gate in c:
    print gate
