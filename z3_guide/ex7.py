from z3 import *

i,j = Ints('i j')
a = Array('a',IntSort(), IntSort())
b = Update(a,3,1)

print a
print b
prove(Implies(j!=3, a[j]==a[j]))
prove(b[3]==1)
prove(Select(Store(a,0,5),0) == 5)
print eq(Select(a,0), a[0])
solve(a[0]==0)

