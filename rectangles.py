import random
import math
import matplotlib.pyplot as plt

# Rect(Tuple(int x,int y) p1 ,Tuple(int x,int y) p2,Tuple(int x,int y) p3,Tuple(int x,int y) p4)
# Rectangle class containing all the points for an individual rectangle.
class Rect:
    def __init__(self,p1,p2,p3,p4):
        self.p1=p1
        self.p2=p2
        self.p3=p3
        self.p4=p4

    # getLines()
    # Returns the lines of the rectangle.
    # p1 -> p3, p4 -> p2, p3 -> p4, p1 -> p2
    def getLines(self):
        return ((self.p1,self.p3),(self.p4,self.p2),(self.p3,self.p4),(self.p1,self.p2))

# ccw(p0,p1,p2): Int (-1,0,1)
#
def ccw(p0, p1, p2):
    dx1 = p1[0] - p0[0]
    dy1 = p1[1] - p0[1]
    dx2 = p2[0] - p0[0]
    dy2 = p2[1] - p0[1]
    if dx1 * dy2 > dy1 * dx2: return 1
    if dx1 * dy2 < dy1 * dx2: return -1
    return 0

# intersect(l1,l2): Int
# Determine if two lines intersect
def intersect(l1, l2):
    return (ccw(l1[0], l1[1], l2[0]) *
            ccw(l1[0], l1[1], l2[1]) <= 0 and
            ccw(l2[0], l2[1], l1[0]) *
            ccw(l2[0], l2[1], l1[1]) <= 0)


# rotate(Tuple (int x,int y) origin,Tuple (int x,int y) point,Float angle): int qx, int qy
# Rotates a point using a reference point, origin and angle to rotate by.
def rotate(origin,point,angle):

    # Split point, origin into x and y
    ox,oy=origin
    px,py=point

    # Rotate px and py by angle 'angle' with respect to ox and oy
    qx = ox + math.cos(angle) * (ox-ox)-math.sin(angle)*(py-oy)
    qy = oy + math.sin(angle) * (px-ox)+math.cos(angle)*(py-oy)

    return qx, qy


# genrect()
# Generates a random rectange.
def genrect():

    w=random.randint(5,10)
    h=random.randint(5,10)
    x=random.randint(0,8)
    y = random.randint(0,8)
    angle=random.randint(0,360)

    # Bottom Left Point
    p1 = [x,y]

    # Top Left Point
    p2 = [x,y+h]

    # Bottom Right Point
    p3 = [x+w,y]

    # Top Right Right Point
    p4 = [x+w,y+h]

    # Midpoint of rectangle
    a = (math.fabs((p1[0] + p3[0]) / 2), math.fabs((p2[1] + p4[1])) / 2)

    # Rotate each poing by 'angle', using a as a reference origin
    p1 = rotate(a,p1,angle)
    p2 = rotate(a,p2,angle)
    p3 = rotate(a,p3,angle)
    p4 = rotate(a,p4,angle)

    # Generate a new rectangle using the points and return it
    r = Rect(p1,p2,p3,p4)
    return r


# checkintersect(Rect r1,Rect r2)
# Get the number of times two rectangles intersect (if at all)
def checkintersect(r1,r2):
    intersects=0

    s1=r1.getLines()
    s2=r2.getLines()

    # Check that each side of both rectangles does not collide with another side
    # If it does, incremenent intersects.
    for i in range(len(s1)):
        for j in range (len(s2)):
            if intersect(s1[i],s2[j]) == True:
                intersects += 1

    return intersects


# checkcontains(Rect r1,Rect r2)
# Check if r1 is contained within r2 without making contact
# If this function returns an intersect of one, r1 is contained within r2.
def checkcontains(r1,r2):
    intersects=0
    s=r2.getLines()
    ln = ((r1.p1), (r1.p1[0], r1.p1[0] + 1000))

    # If an intersection is found, increment intersects
    for i in range(len(s)):
        if intersect(ln,s[i])==True:
            intersects+=1

    return intersects


# plotrects(Rect r1,Rect r2)
# Plots the rectangle on a matplot and calls checkintersect, checkcontains.
def plotrects(r1,r2):
    plt.plot([r1.p1[0], r1.p3[0], r1.p4[0], r1.p2[0],r1.p1[0]], [r1.p1[1], r1.p3[1], r1.p4[1], r1.p2[1],r1.p1[1]])
    plt.plot([r2.p1[0], r2.p3[0], r2.p4[0], r2.p2[0], r2.p1[0]], [r2.p1[1], r2.p3[1], r2.p4[1], r2.p2[1], r2.p1[1]])

    # If r1 is inside r2
    ctns = checkcontains(r1, r2)
    if ctns == 1:
        plt.title("Rectangle is contained within other rectangle.")

    # if r2 is inside r1
    else:
        ctns = checkcontains(r2, r1)
        if ctns == 1:
            plt.title("Rectangle is contained within other rectangle.")

    if ctns != 1:
        intr=checkintersect(r1,r2)
        if intr > 0:
            plt.title("Intersect Found! Intersects: "+str(intr))
        else:
            plt.title("No intersections found.")

    # Window Settings
    wsize = 640
    plt.axis([0,32,0,32])
    plt.grid()
    plt.show()

# Random Rectangle Demonstration
t1 = genrect()
t2 = genrect()
print(t1.p1,t1.p2,t1.p3,t1.p4)
print(t2.p1,t2.p2,t2.p3,t2.p4)
plotrects(t1,t2)

# Rectangles contained demonstration
t3=Rect((4,4),(16,4),(4,16),(16,16))
t4=Rect((8,8),(12,8),(8,12),(12,12))

plotrects(t3,t4)