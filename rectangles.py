from tkinter import Tk, Canvas, Frame, BOTH
import random
import cmath, math


class window(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

    def print_rect(self, r):
        self.parent.title = ("Rectangles.py")
        self.pack(fill=BOTH, expand=1)

        c = Canvas(self)
        c.create_line(r.x, r.y, r.x + r.l, r.y)
        c.create_line(r.x, r.y, r.x, r.y + r.h)

        c.pack(fill=BOTH, expand=1)


class rect:
    def __init__(self, x, y, l, h, r):
        self.x = x
        self.y = y
        self.l = l
        self.h = h

    def get_overlap(self, other):
        pass



root = Tk()
view = window(root)
#r = make_rect()
r = rect(0,0,255,255,0)
view.print_rect(r)
root.geometry("400x250+300+300")
root.mainloop()