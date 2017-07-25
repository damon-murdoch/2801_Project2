import sys

# Laddergram(file)
# Allows the user to convert one equal length word to another.
class Laddergram:

    # Laddergram(file)
    def __init__(self,file):
        self.stack = []
        self.visited = []
        self.steps=0
        self.f = open(file,'r')

    # gen_dict(String a):
    # Creates a new dictionary containing all the words with the same character number as 'a'.
    def gen_dict(self,a):

        d = []
        for line in self.f:
            line=line.rstrip()
            if len(line) == len(a):
                d.append(line)
        return d
    # start(String a, String b):
    # Initialises / resets all data structures in the object, passes a and b to the solve recursion algorithm.
    def start(self,a,b):
        self.steps=0
        self.stack=[]
        self.visited=[]
        self.sidwaysmoves = 0
        self.d = self.gen_dict(a)
        out = self.solve(a,b)
        return out

    # get_heuristic(String a,String b):
    # Counts the number of same characters in the same index for a and b.
    def get_heuristic(self,a,b):
        h=0
        if not (len(a)==len(b)):
            return -1
        for i in range(len(a)):
            if a[i]==b[i]:
                h+=1
        return h

    # solve(String a, String b):
    # Reaches word b from word a using recursive backtracking method.
    def solve(self,a,b):

        out = a
        self.steps+=1

        # If a is not the same length of b or either a or b are not in the dictionary
        if len(a) != len(b) or a not in self.d or b not in self.d:
            print("Invalid inputs!")
            return -1

        # Once a and b share a value, it cannot be changed again.
        lock = []
        add=True
        for i in range(len(a)):
            lock.append(a[i]==b[i])

        # If a is equal to be, problem solved.
        if a == b:
            return self.stack

        # Stores all of the possible moves
        s = []

        # Populate S
        for i in range(len(self.d)):
            # if space has not been visited and is no more than 1 character away from a
            if self.d[i] not in self.visited and self.get_heuristic(a,self.d[i])==len(a)-1:
                # If the character changes any locked indexes, refuse
                for j in range(len(self.d[i])):
                    if self.d[i][j]!=a[j] and lock[j] == True:
                        add=False
                # Else add the word to the list, along with the heuristic
                if add==True:
                    s.append((self.d[i],self.get_heuristic(b,self.d[i])))
                add=True

        # Sort S by highest heuristic
        s.sort(key=lambda tup: tup[1], reverse=True)

        # If there are more than zero options in S
        if len(s) > 0:
            # Take the first option, append it to stack and visited
            out = s[0]
            self.stack.append(out[0])
            self.visited.append(out[0])
            # Call solve for the new word
            self.solve(out[0],b)

        # If nothing in S, but items in the stack (Dead-end reached)
        elif len(self.stack) > 0:
            # Return to previous position and retry
            self.solve(self.stack.pop(),b)
        # Else if no possible moves, fail the conversion
        else:
            return -1

# Run-time Variables
l = Laddergram('dictionary.txt')
a = input("Enter Starting word: ").lower().rstrip()
b = input("Enter finishing word:").lower().rstrip()

s=l.start(a,b)
if b in l.stack:
    print("Solution found!")
else:
    print("Solution not reached.")

for i in l.stack:
    print(i.title())
print("Changes: "+str(len(l.stack)))

wait = input("Press any key to exit")