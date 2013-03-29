from revsim import *

c = Cascade({'x1':1, 'x2':1, 'x3':1, 'x4':1, 'f1':0, 'f2':0, 'f3':0, 'f4':0, 'f5':0},
            ['f1', 'f2', 'f3', 'f4', 'f5'])

c.append(Toffoli(['x1', 'x2', 'x4'], 'f1'))
c.append(Toffoli(['x1', 'x3'], 'f1'))
c.append(Toffoli(['x2', 'x4'], 'f1'))
c.append(Toffoli(['f1'], 'f3'))
c.append(Toffoli(['x1', 'x2', 'x4'], 'f4'))
c.append(Toffoli(['x1', 'x3'], 'f4'))
c.append(Toffoli(['f4'], 'f5'))
c.append(Toffoli(['x1', 'x2', 'x4'], 'f2'))

# This is so terrible
cube_list = {}

for gate in c:
    for label in c.constant_line_labels():
        if gate.get_target() == label:
            try:
                cube_list[tuple(gate.get_controls())].append(label)
            except KeyError:
                cube_list[tuple(gate.get_controls())] = [label]

# select all cubes shared by a given key
shared_key_values = {}
for key in cube_list:
    if key[0] in c.constant_line_labels():
        shared_key_values[key] = cube_list[key]

for item in shared_key_values:
    shared_key = item[0]
    shared_value = shared_key_values[item]
    for key in cube_list:
        if shared_key in cube_list[key]:
            cube_list[key] += shared_value
    del cube_list[item]

for key in cube_list:
    print key, sorted(cube_list[key])
