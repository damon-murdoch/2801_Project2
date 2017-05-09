import sys

class lettergram:

    def __init__(self,file):
        self.stack = []
        self.steps=0
        self.sidwaysmoves=0
        self.f = open(file,'r')

    def gen_dict(self,a):

        d = []
        for line in self.f:
            line=line.rstrip()
            if len(line) == len(a):
                d.append(line)
        return d

    def SameChars(self,a,b,c):

        aas=0
        bbs=0
        if len(a) != len(b):
            return -1
        for i in range(len(a)):
            if a[i] == c[i]:
                aas+=1
                pass
            elif  b[i]== c[i]:
                bbs+=1
                pass
        return (aas,bbs)

    def start(self,a,b):

        self.steps=0
        self.stack=[]
        self.sidwaysmoves = 0
        self.d = self.gen_dict(a)
        out = self.recursionsolve(a,b,0,0)
        return out

    def recursionsolve(self,a,b,repeats,found):

        out = a
        self.steps+=1
        if len(a) != len(b) or a not in self.d or b not in self.d:
            return -1
        h=0
        if a == b:
            print(self.stack)
            return 1
        for i in range(len(a)):
            if a[i]==b[i]:
                h+=1
            pass
        s = []
        b = []
        for i in range(len(self.d)):
            sc = self.SameChars(a,b,self.d[i])
            if sc[0] == 3:
                if sc[1] == 1:
                    s.append(self.d[i])
                # Not an optimal move
                else:
                    b.append(self.d[i])
        print("S",s)
        print("H",self.stack)
        if len(s) > repeats:
            out = s[repeats]
            self.stack.append(out)
            self.recursionsolve(out,b,0,found+1)
        else:
            self.recursionsolve(out, b, 0, found + 1)
            '''
            if len(self.stack) > 0:
                self.recursionsolve(self.stack.pop(),b,repeats+1,found-1)
            else:
                return -1
            '''
# Run-time Variables
l = lettergram('dictionary.txt')
a = input("Enter Starting word: ").lower()
b = input("Enter finishing word:").lower()
print(a,b)
s=l.start(a,b)
print(s)
if s != -1:
    sys.stdout.write("Conversion performed! Steps: "+str(l.steps)+"\n")
else:
    print("Conversion failed.")