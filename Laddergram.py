import sys

class lettergram:
    def __init__(self,file):

        self.stack = []
        self.f = open(file,'r')

    def gen_dict(self,a):
        d = []
        for line in self.f:
            if len(line) == len(a)+1:
                d.append(line.strip())
        return d

    def solve(self,a,b):

        self.d = self.gen_dict(a)
        #print(self.d)

        steps = 0
        out = a
        changed=False

        if len(a) != len(b):
            return -1

        print(a)

        while (out != b):
            for i in range(len(a)):
                if out[i] != b[i]:
                    temp = out
                    if i < len(a) - 1:
                        out = out[:i] + b[i] + out[i + 1:]
                        #print(out)
                    else:
                        out = out[:i] + b[i]
                        #print(out)

                    if out not in self.d:
                        out = temp
                    else:
                        changed = True
                        print(out)
                        steps += 1
            if changed == False:
                return -1
            changed=False
        return steps

# Run-time Variables
l = lettergram('dictionary.txt')
a = input("Enter Starting word: ")
b = input("Enter finishing word:")
s=l.solve(a,b)
if s > -1:
    sys.stdout.write("Conversion performed! Steps: "+str(s)+"\n")
else:
    print("Conversion failed.")