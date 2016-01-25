from z3 import *

i,j = Ints('i j')
def prime_nat(n):
   return Not(Exists([i,j],And(i>1,j>1, n==i*j) ))

prove(ForAll(i, Exists(j, j>i)))
prove(prime_nat(5))


