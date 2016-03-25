import sys

# Checks the usage in the command line
if len(sys.argv) != 2:
    print "Usage: python bricks.py <num_bricks>"
    sys.exit(0)

# get the starting number of bricks
bricks = int(sys.argv[1])

# ------- create the NuSMV code ----------- #

linebreak = lambda a,b: a+"\n"+b

# module declaration and variable declaration
main = """MODULE main
VAR
    bricks : 0..{0}; 
    i : 1..3;
    j : 1..3;
    turn : boolean;
    winner : {{none, a, b}};
ASSIGN""".format(bricks)

#TODO the initialization of variables
init = "" 


#TODO transitions
next = ""


#TODO the specifications 
spec = ""

# put it all together
print reduce(linebreak, [main,init,next,spec])

