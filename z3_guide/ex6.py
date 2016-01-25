from z3 import *

p, q = Bools('p q')
demorgan = And(p, q) == Not(Or(Not(p), Not(q)))
prove(demorgan)	
