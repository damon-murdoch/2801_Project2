import sys

class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

class lettergram:

    def __init__(self,file):

        self.stack = []
        self.visited = []
        self.f = open(file,'r')

    def gen_dict(self,a):

        d = []
        for line in self.f:
            line=line.rstrip()
            if len(line) == len(a):
                d.append(line)
        return d

    def SameChars(self,a,b,c)
        for i in range(len(a)):
            if a[i] == c[i]:
                aas+=1
                pass
            elif  b[i]== c[i]:
                bbs+=1
                pass
        return aas,bbs

    def start(self,a,b):

        self.steps=0
        self.stack=[]
        self.visited=[]
        self.sidwaysmoves = 0
        self.d = self.gen_dict(a)
        out = self.recursionsolve(a,b,0)
        return out

    def recursionsolve(self,a,b,repeats):

        out = a
        self.steps+=1
        if len(a) != len(b) or a not in self.d or b not in self.d:
            print ("Invalid inputs!")
            return -1
        if a == b:
            #print(self.stack)
            return 1
        s = []
        x = []

        # Populate S
        for i in range(len(self.d)):
            sc = self.SameChars(a,b,self.d[i])
            #print(sc)
            if sc[0] == 3:
                if sc[1] == 1:
                    s.append(self.d[i])
                # Not an optimal move
                else:
                    x.append(self.d[i])

        print("Options",s)
        print("Stack",self.stack)
        print("Visited",self.visited)
        if len(s) > repeats:
            out = s[repeats]
            self.stack.append(out)
            self.recursionsolve(out,b,0)
        else:
            if len(x) > repeats:
                if x[repeats] not in self.visited:
                    out = x[repeats]
                    self.stack.append(out)
                    self.visited.append(out)
                    self.recursionsolve(out,b,0)
                else:
                    self.recursionsolve(out,b,repeats+1)

            elif len(self.stack) > 0:
                self.recursionsolve(self.stack.pop(),b,repeats+1)
            else:
                return -1

# Run-time Variables
l = lettergram('dictionary.txt')
a = input("Enter Starting word: ").lower().rstrip()
b = input("Enter finishing word:").lower().rstrip()
print(a,b)
s=l.start(a,b)
print(s)
if s != -1:
    sys.stdout.write("Conversion performed! Steps: "+str(l.steps)+"\n")
else:
    print("Conversion failed.")
