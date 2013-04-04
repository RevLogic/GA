from shared_cube import *

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

s = SharedCube(c)
s.generate()
