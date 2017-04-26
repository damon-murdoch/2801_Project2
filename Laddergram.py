import sys

class lettergram:
    def __init__(self,file):

        self.stack = []
        self.f = open(file,'r')
        self.d = self.f.read().splitlines()

    def solve(self,a,b):
        steps = 0
        out = a
        if a > b:
            smallest = b
        else:
            smallest = a

        changed = False

        print(a)

        while (out != b):
            for i in range(len(smallest)):
                if out[i] != b[i]:
                    temp = out
                    if i < len(smallest) - 1:
                        out = out[:i] + b[i] + out[i + 1:]
                    else:
                        out = out[:i] + b[i]

                    if out not in self.d:
                        sys.stdout.write("Attempted "+str(out)+"\n")
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