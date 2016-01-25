# The problem is solve the following puzzle. There are three types of tiles, A,B, and C. You 
# are given a string of them, and the goal is to reduce the string to nil (empty) while following
# the rules of the game. A sample input might be
#     CCAAAABBBACC
# and a valid move is the removal of 3 or more continguous tiles of the same type. For example,
# a valid move here is removing the 3 Bs. However, a contiguous block of tiles must be removed in its
# entirety. This means that you cannot remove just 3 of the 4 A's appearing at the start, but you must
# remove all of them. A winning sequence of moves is a sequence of valid moves that reduces the string to nil
# For example, here is how to win with the example:
#     CCAAAABBBACC
#     CCAAAAACC
#     CCCC
#     nil
# For some inputs the game is unwinnable. Here is the game's encoding into satisfiability. 

# This solution is adapted from Charuvit Wannissorn's solution
# My solution was uglier, although it did not use Z3 arrays

import sys
from z3 import *

# Checks the usage in the command line
if len(sys.argv) != 3:
    print "Usage: python tiling.py <input_file> <output_file>"
    sys.exit(0)

# Opens the files passed in the command line
_in = open(sys.argv[1], "r")
_out = open(sys.argv[2], "w")

# Reads the input file
s = _in.readline()

# a Z3 solver instance
solver = Solver()

#########################################################
# Helper variable definitions, Z3 variables + functions #
#########################################################

# The general strategy is to have a sequence of arrays representing
# the state of the game after each move. The number of moves in the 
# game depends on the input, but the max number of move possible is
# len(s)/3, making len(s)/3+1 states. 
N = len(s)/3 + 1    


# We will keep track of len(s)/3 + 1 states, the indices (start and
# end) of the reduction in each state, and the length of the string
# for each state.
X = [ Array("x_%s" % i, IntSort(), IntSort()) for i in range(N) ]
start = [ Int("start_%s" % i) for i in range(N) ]
end = [ Int("end_%s" % i) for i in range(N) ]
L = [ Int("l_%s" % i) for i in range(N) ]
k = Int('k')

#########################################################
#        The actual constraints for the problem         #
#########################################################

# The initial state corresponds to the input. Z3 has no char datatype, so
# we map each character to an integer using the built-in ord function
instance_c = [ X[0][j] == ord(s[j]) for j in range(len(s)) ]

# The initial length is the input length, and the final length is zero
instancelen_c = [ L[0] == len(s), L[N-1] == 0]

# This is the core bunch of constraints
reduce_c = [
            # If the string has been reduced to nil in this state, the next state is the same. Otherwise,
            If(L[i-1]==0, L[i]==0, 
                  And(
                      # The reduction indices are in range of the string in this state
                      # and the block being reduced is at least of size 3
                      0 <= start[i], start[i]+3 <= end[i], end[i] <= L[i-1],

                      # The substring up to the start of the reduction is the same for this state and the next
                      ForAll(k, Implies(And(       0 <= k, k < start[i]),  X[i-1][k] == X[i][k])), 
                      # The substring being reduced consists of only one type of character
                      ForAll(k, Implies(And(start[i] <= k, k < end[i]-1),  X[i-1][k] == X[i-1][k+1])),
                      # The substring after the end of the reduction is the same for this state and the next
                      ForAll(k, Implies(And(  end[i] <= k, k < L[i-1]),    X[i-1][k] == X[i][k + start[i] - end[i]])),

                      # No adjacent characters of the same type before the start of the reduction
                      Or(start[i]==0, Not(X[i-1][start[i]-1] == X[i-1][start[i]])),
                      # No adjacent characters of the same type after the end of the reduction
		      Or(end[i]==L[i-1], Not(X[i-1][end[i]-1] == X[i-1][end[i]])),

                      # The length of the string in the next state is the length of the current, minus the length of the reduction
                      L[i] == L[i-1] + start[i] - end[i]
                     )
              )
    for i in range(1,N)]

# add all constraints to the solver
solver.add(instance_c + instancelen_c + reduce_c)

isSAT = solver.check()
if isSAT == sat:
    m = solver.model()
    # Get the start and end indices of the reductions from the model   
    red = [map(lambda x:m[x[i]].as_long(), [start,end]) for i in range(N) if m[start[i]] != None] 
    for i in range(len(red)):        
        # Add brackets around the substring being reduced
        start,end = red[i][0],red[i][1]
        _out.write(s[:start] + "(" + s[start:end]+ ")" + s[end:] + "\n")
        s = s[:start] + s[end:]
    _out.write("nil")
else:
    _out.write("no solution possible")

