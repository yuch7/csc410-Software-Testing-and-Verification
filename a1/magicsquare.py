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
sum_in = int(sys.argv[2])
dimension_in = int(sys.argv[1])
array_h = [[Int('x%sy%s' % (j, i)) for i in range(dimension_in)] for j in range(dimension_in)]
array_v = [[array_h[i][j] for i in range(dimension_in)] for j in range(dimension_in)]
diagonal_l = [array_h[i][i] for i in range(dimension_in)]
diagonal_r = [array_h[dimension_in - i - 1][i] for i in range(dimension_in)]

#########################################################
#        The actual constraints for the problem         #
#########################################################

##################  Your Code Here  #####################
horizontal_c = [sum(array_h[i]) == sum_in for i in range(dimension_in)]
vertical_c = [sum(array_v[i]) == sum_in for i in range(dimension_in)]
diagonal_lc = [sum(diagonal_l) == sum_in]
diagonal_rc = [sum(diagonal_r) == sum_in]

#########################################################
#         Call the solver and print the answer          #
#########################################################

# The final formula going in. Change this to your actual formula
F = horizontal_c + vertical_c + diagonal_rc + diagonal_lc

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
   print "SAT %s" % m
else:
   print "UNSAT"

