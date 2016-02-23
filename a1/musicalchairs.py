import sys
from z3 import *

# Checks the usage in the command line
if len(sys.argv) != 2:
    print "Usage: python musicalchairs.py <input_file>"
    sys.exit(0)

# Opens the files passed in the command line for reading/writing
_in = open(sys.argv[1], "r")

#########################################################
# Helper variable definitions, Z3 variables + functions #
######################################################### 

n = int(_in.readline())
S = int(_in.readline())
sub_set = map(int, _in.readline().strip().strip('[').strip(']').split(','))
board = [Int("%s" % i) for i in range(n)]

##################  Your Code Here  #####################

#########################################################
#        The actual constraints for the problem         #
#########################################################

##################  Your Code Here  #####################

must_move = []
for i in range(n):
	if i in sub_set:
		if ((board[i] + S) >= n):
			must_move.append((board[i] >= 0))
			must_move.append((board[i] < i))
	for j in range(n):
		if i != j:
			must_move.append((board[i] != board[j]))

distinct = [Distinct(board)]

in_seats = [(i < n) for i in board]
not_neg = [(i >= 0) for i in board]

#########################################################
#         Call the solver and print the answer          #
#########################################################

# The final formula going in. Change this to your actual formula
F = must_move + distinct + in_seats + not_neg

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
   print "%s" % m
else:
   print "no solution possible"

