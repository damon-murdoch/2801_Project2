import random

import matplotlib.pyplot as plt

def ccw(p0, p1, p2):
    dx1 = p1[0] - p0[0]
    dy1 = p1[1] - p0[1]
    dx2 = p2[0] - p0[0]
    dy2 = p2[1] - p0[1]
    if dx1 * dy2 > dy1 * dx2: return 1
    if dx1 * dy2 < dy1 * dx2: return -1
    return 0

def intersect(l1, l2):
    return (ccw(l1[0], l1[1], l2[0]) *
            ccw(l1[0], l1[1], l2[1]) <= 0 and
            ccw(l2[0], l2[1], l1[0]) *
            ccw(l2[0], l2[1], l1[1]) <= 0)

l1 = [[1,1], [10,10]]
l2 = [[10, 1], [1,9]]
print(l1, l2, intersect(l2, l1))
plt.plot([l1[0][0], l1[1][0]], [l1[0][1], l1[1][1]])
plt.plot([l2[0][0], l2[1][0]], [l2[0][1], l2[1][1]])
plt.axis([0, 12, 0, 12])
plt.show()

class window(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

    def print_rect(self, r1,r2):
        self.parent.title = ("Rectangles.py")
        self.pack(fill=BOTH, expand=1)

        c = Canvas(self)
        c.create_line(r1.x1,r1.y1,r1.x2,r1.y2)
        c.create_line(r1.x2, r1.y2, r1.x4, r1.y4)
        c.create_line(r1.x3, r1.y3, r1.x1, r1.y1)
        c.create_line(r1.x4, r1.y4, r1.x3, r1.y3)

        c.create_line(r2.x1, r2.y1, r2.x2, r2.y2)
        c.create_line(r2.x2, r2.y2, r2.x4, r2.y4)
        c.create_line(r2.x3, r2.y3, r2.x1, r2.y1)
        c.create_line(r2.x4, r2.y4, r2.x3, r2.y3)

        c.pack(fill=BOTH, expand=1)

class rect:
    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):

        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4

        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.y4 = y4

    def get_overlap(self, other):
        pass

wsize=640

root = Tk()
view = window(root)

def genrect():
    w=random.randint(0,256)
    h=random.randint(0,256)
    x=random.randint(0,480)
    y = random.randint(0, 480)
    angle=random.randint(0,360)

    # Top Left
    x1= x-w
    y1= y-h

    # Top Right
    x2= x-w
    y2= y

    # Bottom Left
    x3= x
    y3= y-h

    # Bottom Right
    x4= x
    y4= y

    r = rect(x1,y1,x2,y2,x3,y3,x4,y4)
    return r

r1=genrect()
r2=genrect()

view.print_rect(r1,r2)

root.geometry(str(wsize)+"x"+str(wsize)+"+"+str(wsize)+"+"+str(wsize))
root.mainloop()