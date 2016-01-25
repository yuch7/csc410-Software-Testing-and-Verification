from z3 import *

def prime_nat(n):
   return Not(Exists([i,j],And(i>1,j>1, n==i*j) ))
