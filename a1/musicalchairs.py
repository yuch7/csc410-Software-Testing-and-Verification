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
sub_set = eval(_in.readline())
board = [Int("%s" % i) for i in range(n)]

##################  Your Code Here  #####################

#########################################################
#        The actual constraints for the problem         #
#########################################################

##################  Your Code Here  #####################

must_move = []	
for i in sub_set:
	must_move.append((board[i] != i))
	if ((i + S) >= n):
		tmp1 = Or((board[i] <= (i + S - n)), board[i] > i)
	else:
		tmp1 = (board[i] <= (i + S))
	if ((i - S) < 0):
		tmp2 = Or((board[i] >= (n - i - S)), board[i] < i)
	else:
		tmp2 = (board[i] >= i - S)
	must_move.append(Or(tmp1, tmp2))

cant_move = []
for i in range(n):
	if i not in sub_set:
		cant_move.append((board[i] == i))

distinct = [Distinct(board)]

in_seats = [(i < n) for i in board]
not_neg = [(i >= 0) for i in board]

#########################################################
#         Call the solver and print the answer          #
#########################################################

# The final formula going in. Change this to your actual formula
F = must_move + distinct + in_seats + not_neg + cant_move

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
   ret = [[i, m.eval(board[i])] for i in range(n)]
   print "%s" % ret
else:
   print "no solution possible"

