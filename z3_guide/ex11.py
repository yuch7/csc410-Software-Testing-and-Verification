from z3 import *

x = Int('x')
y = Int('y')
a = Array('a', IntSort(),IntSort())

s = Solver()
s.add(x > 0, a[x]==y, a[x+1]==y+1)

if s.check() == sat:
    m = s.model()
    print m[x]
    print m[a]
    print a[0]
    print m.eval(x+y)
    print [ m.eval(a[j]) for j in range(3) ]
else:
    print "failed to solve"

solve(Distinct(x,y))
