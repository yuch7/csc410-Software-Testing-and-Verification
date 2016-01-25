import sys
from z3 import *

# Checks the usage in the command line
if len(sys.argv) != 2:
    print "Usage: python strategy.py <input_file>"
    sys.exit(0)

# Opens the files passed in the command line for reading/writing
_in = open(sys.argv[1], "r")

# game matrix
r = []
for i in range(3):
    r = r + [eval(_in.readline())]

#########################################################
# Helper variable definitions, Z3 variables + functions #
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
   # evaluate the final array from the model, and re-map the guest id's to the result
   m = solver.model()   
   
   ##############  Complete the Output  #################
   print "Player A:"
   print "Player B:"
else:
   print "no solution possible"

