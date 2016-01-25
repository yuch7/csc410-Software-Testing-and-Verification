from z3 import *

x = Int('x')
r = Real('r')
a,b = Ints('a b')
y = IntVector('y', 5)
z = [ Int('z%s' % i) for i in range(5) ]
# Create a 3x3 "matrix" (list of lists) of integer variables
X = [ [ Int("x_%s_%s" % (i, j)) for j in range(3) ] 
      for i in range(3) ]

print x.sort(),r.sort(),a.sort()
print y
print z
print X
pp(X)
