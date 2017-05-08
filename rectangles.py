import random
import math
import matplotlib.pyplot as plt

class Rect:
    def __init__(self,p1,p2,p3,p4):
        self.p1=p1
        self.p2=p2
        self.p3=p3
        self.p4=p4

    def getLines(self):
        return ((self.p1,self.p3),(self.p4,self.p2),(self.p3,self.p4),(self.p1,self.p2))

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

def rotate(origin,point,angle):
    ox,oy=origin
    px,py=point
    qx = ox + math.cos(angle) * (ox-ox)-math.sin(angle)*(py-oy)
    qy = oy + math.sin(angle) * (px-ox)+math.cos(angle)*(py-oy)
    return qx, qy

def genrect():
    w=random.randint(5,10)
    h=random.randint(5,10)
    x=random.randint(0,8)
    y = random.randint(0,8)
    angle=random.randint(0,360)

    # Bottom Left
    p1 = [x,y]

    # Top Left
    p2 = [x,y+h]

    # Bottom Right
    p3 = [x+w,y]

    # Top Right Right
    p4 = [x+w,y+h]

    a = (math.fabs((p1[0] + p3[0]) / 2), math.fabs((p2[1] + p4[1])) / 2)

    p1 = rotate(a,p1,angle)
    p2 = rotate(a,p2,angle)
    p3 = rotate(a,p3,angle)
    p4 = rotate(a,p4,angle)

    r = Rect(p1,p2,p3,p4)
    return r

def checkintersect(r1,r2):
    intersects=0

    s1=r1.getLines()
    s2=r2.getLines()

    for i in range(len(s1)):
        for j in range (len(s2)):
            if intersect(s1[i],s2[j]) == True:
                intersects += 1

    return intersects

def checkcontains(r1,r2):
    intersects=0
    s=r2.getLines()
    ln = ((r1.p1), (r1.p1[0], r1.p1[0] + 1000))

    for i in range(len(s)):
        if intersect(ln,s[i])==True:
            intersects+=1

    return intersects

def plotrects(r1,r2):
    plt.plot([r1.p1[0], r1.p3[0], r1.p4[0], r1.p2[0],r1.p1[0]], [r1.p1[1], r1.p3[1], r1.p4[1], r1.p2[1],r1.p1[1]])
    plt.plot([r2.p1[0], r2.p3[0], r2.p4[0], r2.p2[0], r2.p1[0]], [r2.p1[1], r2.p3[1], r2.p4[1], r2.p2[1], r2.p1[1]])

    ctns = checkcontains(r1, r2)
    if ctns ==1:
        plt.title("Rectangle is contained within other rectangle. Intersects: "+str(ctns))

    else:
        ctns = checkcontains(r2, r1)
        if ctns == 1:
            plt.title("Rectangle is contained within other rectangle. Intersects: " + str(ctns))

    if ctns != 1:
        intr=checkintersect(r1,r2)
        if intr > 0:
            plt.title("Intersect Found! Intersects: "+str(intr))
        else:
            plt.title("No intersections found.")

    plt.axis([0,32,0,32])
    plt.grid()
    plt.show()

t1 = genrect()
t2 = genrect()

plotrects(t1,t2)

t3=Rect((4,4),(16,4),(4,16),(16,16))
t4=Rect((8,8),(12,8),(8,12),(12,12))

plotrects(t3,t4)