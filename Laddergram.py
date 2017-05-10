import sys

class lettergram:

    def __init__(self,file):
        self.stack = []
        self.visited = []
        self.steps=0
        self.f = open(file,'r')

    def gen_dict(self,a):

        d = []
        for line in self.f:
            line=line.rstrip()
            if len(line) == len(a):
                d.append(line)
        return d

    def same_chars(self,a,c):
        ac=0
        for i in range(len(a)):
            if a[i] == c[i]:
                ac+=1
                pass
        return ac

    def start(self,a,b):

        self.steps=0
        self.stack=[]
        self.visited=[]
        self.sidwaysmoves = 0
        self.d = self.gen_dict(a)
        out = self.solve(a,b)
        return out

    def get_heuristic(self,a,b):
        h=0
        if not (len(a)==len(b)):
            return -1
        for i in range(len(a)):
            if a[i]==b[i]:
                h+=1
        return h

    def solve(self,a,b):

        out = a
        self.steps+=1
        #print(a,b)
        lock = []
        add=True
        for i in range(len(a)):
            lock.append(a[i]==b[i])
        #print(lock)
        if len(a) != len(b) or a not in self.d or b not in self.d:
            print("Invalid inputs!")
            return -1

        if a == b:
            return self.stack

        s = []

        # Populate S
        for i in range(len(self.d)):
            if self.d[i] not in self.visited and self.same_chars(a,self.d[i])==len(a)-1:
                for j in range(len(self.d[i])):
                    if self.d[i][j]!=a[j] and lock[j] == True:
                        add=False
                if add==True:
                    s.append((self.d[i],self.get_heuristic(b,self.d[i])))
                add=True

        s.sort(key=lambda tup: tup[1], reverse=True)

        if len(s) > repeats:
            out = s[repeats]
            self.stack.append(out[0])
            self.visited.append(out[0])
            self.solve(out[0],b)

        elif len(self.stack) > 0:
            self.solve(self.stack.pop(),b)
        else:
            return -1

# Run-time Variables
l = lettergram('dictionary.txt')
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
