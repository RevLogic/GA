from revsim import *

a = arg(1)
b = arg(2)
c = arg(3)

lines = [a,b,c]
c = Cascade(lines)
c.append(fred, [0], [1,2])
print c.run()
