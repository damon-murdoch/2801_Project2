from tkinter import Tk, Canvas, Frame, BOTH
import random
import cmath, math


class window(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

    def print_rect(self, r1,r2):
        self.parent.title = ("Rectangles.py")
        self.pack(fill=BOTH, expand=1)

        c = Canvas(self)
        c.create_line(r1.x1,r1.y1,r1.x2,r1.y2)
        c.create_line(r1.x2, r1.y2, r1.x3, r1.y3)
        c.create_line(r1.x3, r1.y3, r1.x4, r1.y4)
        c.create_line(r1.x4, r1.y4, r1.x1, r1.y1)

        c.create_line(r2.x1, r2.y1, r2.x2, r2.y2)
        c.create_line(r2.x2, r2.y2, r2.x3, r2.y3)
        c.create_line(r2.x3, r2.y3, r2.x4, r2.y4)
        c.create_line(r2.x4, r2.y4, r2.x1, r2.y1)

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

wsize=360

root = Tk()
view = window(root)
#r = make_rect()
r1 = rect(5,5,255,5,255,255,5,255)
r2 = rect(25,25,275,25,275,275,25,275)

view.print_rect(r1,r2)
#root.geometry("512x512+512+512")
root.geometry(str(wsize)+"x"+str(wsize)+"+"+str(wsize)+"+"+str(wsize))
root.mainloop()