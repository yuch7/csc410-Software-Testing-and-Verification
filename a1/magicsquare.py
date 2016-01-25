import sys
from z3 import *

# Checks the usage in the command line
if len(sys.argv) != 3:
    print "Usage: python magicsquare.py <dimension> <sum>"
    sys.exit(0)

#########################################################
#     Helper variables, functions, and Z3 variables     #
######################################################### 

##################  Your Code Here  #####################

#########################################################
#        The actual constraints for the problem         #
#########################################################

##################  Your Code Here  #####################


#########################################################
#         Call the solver and print the answer          #
#########################################################

# The final formula going in. Change this to your actual formula
F = simplify(Bool('p')==Bool('p'))

# a Z3 solver instance
solver = Solver()
# add all constraints
solver.add(F)
# run Z3
isSAT = solver.check()
# print the result
if isSAT == sat:
   m = solver.model()
  
   ##############  Complete the Output  #################
   print 
else:
   print "UNSAT"

