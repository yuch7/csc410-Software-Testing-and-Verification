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

aWin = Bool("aWin")
aHigh = Bool("aHigh")
aMed = Bool("aMed")
aLow = Bool("aLow")

bWin = Bool("bWin")
bHigh = Bool("bHigh")
bMed = Bool("bMed")
bLow = Bool("bLow")

board = []
for i in range(3):
	board.append([])
	for j in range(3):
		board[i].append(Bool("%s%s" % (i, j)))

#########################################################
#        The actual constraints for the problem         #
#########################################################

##################  Your Code Here  #####################

boardc = []
for i in range(3):
  for j in range(3):
    boardc.append(board[i][j] == (r[i][j][0] < r[i][j][1]))
wins = []
wins.append(aWin == (aHigh or aMed or aLow))
wins.append(bWin == (bHigh or bMed or bLow))

eq = []
eq.append(aHigh == reduce(lambda x,y: And(x,y), board[0], True))
eq.append(aMed  == reduce(lambda x,y: And(x,y), board[1], True))
eq.append(aLow  == reduce(lambda x,y: And(x,y), board[2], True))
eq.append(bHigh == reduce(lambda x,y: And(x,y), [board[i][0] for i in range(3)], True))
eq.append(bMed  == reduce(lambda x,y: And(x,y), [board[i][1] for i in range(3)], True))
eq.append(bLow  == reduce(lambda x,y: And(x,y), [board[i][2] for i in range(3)], True))


#########################################################
#         Call the solver and print the answer          #
#########################################################

# The final formula going in. Change this to your actual formula
F = eq + wins + boardc

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
  aStrategy = "High" if is_true(m.eval(aHigh)) else \
    "Med" if is_true(m.eval(aMed)) else \
    "Low" if is_true(m.eval(aLow)) else "No dominant strategy"
  bStrategy = "High" if is_true(m.eval(bHigh)) else \
    "Med" if is_true(m.eval(bMed)) else \
    "Low" if is_true(m.eval(bLow)) else "No dominant strategy"
  print "Player A: The dominant strategy is %s" % aStrategy 
  print "Player B: The dominant strategy is %s" % bStrategy
else:
  print "no solution possible"

