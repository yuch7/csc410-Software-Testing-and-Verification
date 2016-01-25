from z3 import *

x,y = Reals('x y')
a,b,c = Ints('a b c')

solve(a > b + 2,
      a == 2*c + 10,
      c + b <= 1000)

q = Q(1,3)
print x + c + 1
print ToReal(c) + x
print q, q.sort()

