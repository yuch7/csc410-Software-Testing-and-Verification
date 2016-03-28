import sys
from copy import deepcopy
# This code is meant to read in a list of moves for a rubik's cube and generate NuSMV code that solves the cube. 

# To minimize the number of moves, only a surface panel can be turned, and only right.
# So no rotation of central panels, and no left turns. Both achievable from right
# turns of surface panels. Hence the input is simple a list of integers in 0..5
# where an integer represents the panel being turned. 

#Each panel of the cube is numbered 0..5 with 4 being the top and 5 the bottom.
#Here is a graphical representation
#
#       4 4 4
#       4 4 4
#       4 4 4 
# 0 0 0 1 1 1 2 2 2 3 3 3
# 0 0 0 1 1 1 2 2 2 3 3 3
# 0 0 0 1 1 1 2 2 2 3 3 3
#       5 5 5
#       5 5 5 
#       5 5 5 

# Checks the usage in the command line
if len(sys.argv) != 2:
    print "Usage: python rubik.py <input_file>"
    sys.exit(0)

# Opens the file passed in the command line for reading
_in = open(sys.argv[1], "r")

# read the list
moves = eval(_in.readline())

#the rubik's cube in its initial solved state. 
cube = [[[ k for i in range(3)] for j in range(3)] for k in range(6)]

#The relationship of the panels to each-other is encoded in this dictionary
surface = {0:{"top":4,"bottom":5,"left":3,"right":1},
           1:{"top":4,"bottom":5,"left":0,"right":2},
           2:{"top":4,"bottom":5,"left":1,"right":3},
           3:{"top":4,"bottom":5,"left":2,"right":0},
           4:{"top":3,"bottom":1,"left":0,"right":2},
           5:{"top":1,"bottom":3,"left":0,"right":2},
}


# rotate a face (0..5) of the rubik's cube
def rotate(face):
  tmp = deepcopy(cube[face])     
  cube[face][0][0] = tmp[2][0]
  cube[face][0][1] = tmp[1][0]
  cube[face][0][2] = tmp[0][0]
  cube[face][1][0] = tmp[2][1]
  cube[face][1][2] = tmp[0][1]
  cube[face][2][0] = tmp[2][2]
  cube[face][2][1] = tmp[1][2]
  cube[face][2][2] = tmp[0][2]
  tmptop = deepcopy(cube[surface[face]['top']][2])
  tmpbot = deepcopy(cube[surface[face]['bottom']][0])
  tmpleft = [cube[surface[face]['left']][i][2] for i in range(3)]
  tmpright = [cube[surface[face]['right']][i][0] for i in range(3)]
  tmpleft.reverse()
  tmpright.reverse()
  cube[surface[face]['top']][2] = tmpleft
  cube[surface[face]['bottom']][0] = tmpright
  cube[surface[face]['left']][0][2] = tmpbot[0]
  cube[surface[face]['left']][1][2] = tmpbot[1]
  cube[surface[face]['left']][2][2] = tmpbot[2]
  cube[surface[face]['right']][0][0] = tmptop[0]
  cube[surface[face]['right']][1][0] = tmptop[1]
  cube[surface[face]['right']][2][0] = tmptop[2]

#play a series of moves
def play(move_list):
  if move_list != []:
      rotate(move_list[0])
      play(move_list[1:])

# play the input moves
play(moves)

# ------- create the NuSMV code ----------- #

linebreak = lambda a,b: a+"\n"+b
instance = cube

# module declaration and variable declaration
main = """MODULE main
VAR
  cube : array 0..5 of array 0..2 of array 0..2;
  face : 0..5
  done : boolean
ASSIGN
"""

# the initialization of variables to the instance
init = "\tdone := FALSE;\n"
for i in range(6):
  for j in range(3):
    for k in range(3):
      init += "\tinit(cube[{0}][{1}][{2}]) := {3};\n".format(i,j,k,cube[i][j][k])

3
next = ""
for i in range(6):
  for j in range(3):
    for k in range(3):
      next += """
  next(cube[{0}][{1}][{2}]) := case
                        face = 0 : {3} 
                        face = 1 : {4}
                        face = 2 : {5}
                        face = 3 : {6}
                        face = 4 : {7}
                        face = 5 : {8}
                      esac;
""".format(i,j,k,)

spec = "" #TODO

# put it all together
print reduce(linebreak, [main,init,next,spec])

