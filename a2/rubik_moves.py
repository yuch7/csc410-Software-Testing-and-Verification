import sys

# Checks the usage in the command line
if len(sys.argv) != 2:
    print "Usage: python rubik_moves.py <input_file>"
    sys.exit(0)

# Opens the files passed in the command line for reading/writing
_in = open(sys.argv[1], "r")

#take only those lines that pertain to the state or move
r = [line.strip() for line in _in if ("i = " in line) or ("State" in line)]

# add place-holders for states that have repeated moves
for i in range(len(r)-1):
   if not ("=" in r[i]) and not ("=" in r[i+1]):
      r[i] = [r[i],"i = -1"]
   else:
      r[i] = [r[i]]

#flatten the list, remove last item (not actual move)
r =  reduce(lambda x,y: x+y, r[:-1])

#extract the actual moves
r = [int(l.split("=")[1]) for l in r if ("=" in l)]

#replace the place-holders with the repeated moves
for i in range(1,len(r)):
   r[i] = r[i-1] if r[i]==-1 else r[i]

#print the move sequence
print r


