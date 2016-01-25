from z3 import *

p = Bool('p')
q = Bool('q')
r = Bool('r')
x = Real('x')

solve(Implies(p, q), r == Not(q), Or(Not(p), r))
solve(Or(x < 5, x > 10), Or(p, x**2 == 2), Not(p))

