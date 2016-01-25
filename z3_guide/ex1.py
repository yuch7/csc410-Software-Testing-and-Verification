from z3 import *

x = Int('x')
y = Int('y')

s = Solver()
s.add(x > 2, y < 10, x + 2*y == 7)

print s.check()
print s.model()
