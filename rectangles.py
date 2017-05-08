import random
import math
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

class Rect:
    def __init__(self,p1,p2,p3,p4,angle):
        self.a = (math.fabs((p1[0] + p3[0]) / 2), math.fabs((p2[1] + p4[1])) / 2)
        self.p1=self.rotate(self.a,p1,angle)
        self.p2=self.rotate(self.a,p2,angle)
        self.p3=self.rotate(self.a,p3,angle)
        self.p4=self.rotate(self.a,p4,angle)

    def rotate(self,origin,point,angle):
        ox,oy=origin
        px,py=point
        qx = ox + math.cos(angle) * (ox-ox)-math.sin(angle)*(py-oy)
        qy = oy + math.sin(angle) * (px-ox)+math.cos(angle)*(py-oy)
        return qx, qy

    def get_overlap(self, other):
        pass

wsize=640

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

def genrect():
    w=random.randint(5,10)
    h=random.randint(5,10)
    x=random.randint(0,8)
    y = random.randint(0,8)
    angle=random.randint(0,360)
    #print(x,y,w,h)
    # Bottom Left
    # (X,Y)
    p1 = [x,y]

    # Top Left
    p2 = [x,y+h]

    # Bottom Right
    p3 = [x+w,y]

    # Top Right Right
    p4 = [x+w,y+h]

    r = Rect(p1,p2,p3,p4,angle)
    return r

def checkintersect(r1,r2):
    out=False



def plotrects(r1,r2):
    #print(r1.p1,r1.p2,r1.p3,r1.p4,r1.a)
    #print(r2.p1, r2.p2, r2.p3, r2.p4, r2.a)

    plt.plot([r1.p1[0], r1.p3[0], r1.p4[0], r1.p2[0],r1.p1[0]], [r1.p1[1], r1.p3[1], r1.p4[1], r1.p2[1],r1.p1[1]])
    plt.plot([r2.p1[0], r2.p3[0], r2.p4[0], r2.p2[0], r2.p1[0]], [r2.p1[1], r2.p3[1], r2.p4[1], r2.p2[1], r2.p1[1]])

    plt.axis([0,32,0,32])
    plt.grid()
    plt.show()

r1 = genrect()
r2 = genrect()

plotrects(r1,r2)