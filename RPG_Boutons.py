#!/usr/bin/env python3

from tkinter import *
import random
import tkinter as Untitled

XGRID = 20
YGRID = 20
WIDTH = 6
"""
fenetre = Untitled.Tk()
photo = Untitled.PhotoImage(file='28301.gif')
label = Untitled.Label(fenetre, image=photo)
label.pack()
""" 
class Array:

    class Cancelled(BaseException):
        pass

    def __init__(self, master, data=None):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack(fill=X)
        self.label = Label(self.frame)
        self.label.pack()
        self.canvas = Canvas(self.frame)
        self.canvas.pack()
        self.report = Label(self.frame)
        self.report.pack()
        self.left = self.canvas.create_line(0, 0, 0, 0)
        self.right = self.canvas.create_line(0, 0, 0, 0)
        self.pivot = self.canvas.create_line(0, 0, 0, 0)
        self.items = []
        self.size = self.maxvalue = 0
        if data:
            self.setdata(data)

    def setdata(self, data): #  
        olditems = self.items
        self.items = []
        for item in olditems:
            item.delete()
        self.size = len(data)
        self.maxvalue = max(data)
        self.canvas.config(width=(self.size+1)*XGRID, height=(self.maxvalue+1)*YGRID)
        for i in range(self.size):
            self.items.append(ArrayItem(self, i, data[i]))
        self.reset("Sort demo, size %d" % self.size)

    speed = "Sorts"

    def setspeed(self, speed):
        self.speed = speed

    def cancel(self):
        self.message("Cancellé")

    def step(self):
        if self.in_mainloop:
            self.master.quit()

    def wait(self, msecs):
        if self.speed == "Plus Rapide":
            msecs = 0
        elif self.speed == "Rapide":
            msecs = msecs//10
        elif self.speed == "Simple-étape":
            msecs = 1000000000
        if not self.stop_mainloop:
            self.master.update()
            id = self.master.after(msecs, self.master.quit)
            self.in_mainloop = 1
            self.master.mainloop()
            self.master.after_cancel(id)
            self.in_mainloop = 0
        if self.stop_mainloop:
            self.stop_mainloop = 0
            self.message("Cancellé")
            raise Array.Cancelled

    def getsize(self):
        return self.size

    def hide_partition(self): #
        for i in range(self.size):
            item = self.items[i]
            self.canvas.itemconfig(item, fill='red')
        self.hide_left_right_pivot()

    def show_left(self, left):
        if not 0 <= left < self.size:
            self.hide_left()
            return
        x1, y1, x2, y2 = self.items[left].position()
##      top, bot = HIRO
        self.canvas.coords(self.left, (x1 - 2, 0, x1 - 2, 9999))
        self.master.update()

    def show_right(self, right):
        if not 0 <= right < self.size:
            self.hide_right()
            return
        x1, y1, x2, y2 = self.items[right].position()
        self.canvas.coords(self.right, (x2 + 2, 0, x2 + 2, 9999))
        self.master.update()

    def hide_left_right_pivot(self): #
        self.hide_left()
        self.hide_right()
        self.hide_pivot()

    def hide_left(self): #
        self.canvas.coords(self.left, (0, 0, 0, 0))

    def hide_right(self): #
        self.canvas.coords(self.right, (0, 0, 0, 0))

    def hide_pivot(self): #
        self.canvas.coords(self.pivot, (0, 0, 0, 0))

    def reset(self, msg): #
        self.ncompares = 0
        self.nswaps = 0
        self.message(msg)
        self.updatereport()
        self.hide_partition()

    def message(self, msg): #
        self.label.config(text=msg)

    def updatereport(self): #
        text = "%d cmps, %d swaps" % (self.ncompares, self.nswaps)
        self.report.config(text=text)

class ArrayItem:

    def __init__(self, array, index, value): #
        self.array = array
        self.index = index
        self.value = value
        self.canvas = array.canvas
        x1, y1, x2, y2 = self.position()
        self.item_id = array.canvas.create_rectangle(x1, y1, x2, y2,
            fill='green', outline='black', width=1)
        self.canvas.tag_bind(self.item_id, '<Button-1>', self.mouse_down)
        self.canvas.tag_bind(self.item_id, '<Button1-Motion>', self.mouse_move)
        self.canvas.tag_bind(self.item_id, '<ButtonRelease-1>', self.mouse_up)

    def mouse_down(self, event): #
        self.lastx = event.x
        self.lasty = event.y
        self.origx = event.x
        self.origy = event.y
        self.canvas.tag_raise(self.item_id)

    def mouse_move(self, event): #
        self.canvas.move(self.item_id, event.x - self.lastx, event.y - self.lasty)
        self.lastx = event.x
        self.lasty = event.y

    def mouse_up(self, event): #
        i = self.nearestindex(event.x)
        if i >= self.array.getsize():
            i = self.array.getsize() - 1
        if i < 0:
            i = 0
        other = self.array.items[i]
        here = self.index
        self.array.items[here], self.array.items[i] = other, self
        self.index = i
        x1, y1, x2, y2 = self.position()
        self.canvas.coords(self.item_id, (x1, y1, x2, y2))
        other.setindex(here)

    def position(self): #
        x1 = (self.index+1)*XGRID - WIDTH//2
        x2 = x1+WIDTH
        y2 = (self.array.maxvalue+1)*YGRID
        y1 = y2 - (self.value)*YGRID
        return x1, y1, x2, y2

    def nearestindex(self, x):
        return int(round(float(x)/XGRID)) - 1

# Boutons Test

def uniform(array):
    array.message("L'Archer")

def magie(array):
    array.message("Lance Magie")

def distinct(array):
    array.message("Le Black-Mage")

def stepi(array):
    array.message("Le Chef Équipe")

def randomize(array):
    array.message("Le Barbar")

def insertionsort(array):
    array.message("Defance")

def selectionsort(array):
    array.message("Jet Distance")

def bubblesort(array):
    array.message("Soin")

def quicksort(array):
    array.message("Attaque")
        
def demosort(array):
    array.message("Le Guerriseur")

# Sort demo class -- usable as a Grail applet

class SortDemo:
    
    def __init__(self, master, size=15):
        self.master = master
        self.size = size
        self.busy = 0
        self.array = Array(self.master)

        self.botframe = Frame(master)
        self.botframe.pack(side=BOTTOM)
        self.botleftframe = Frame(self.botframe)
        self.botleftframe.pack(side=LEFT, fill=Y)
        self.botrightframe = Frame(self.botframe)
        self.botrightframe.pack(side=RIGHT, fill=Y)

        self.b_qsort = Button(self.botleftframe, text="Attaque", command=self.c_qsort)
        self.b_qsort.pack(fill=X)
        #self.b_qsort.config(state=DISABLED)
        
        self.b_isort = Button(self.botleftframe, text="Defance", command=self.c_isort)
        self.b_isort.pack(fill=X)
        #self.b_isort.config(state=DISABLED)
        
        self.b_ssort = Button(self.botleftframe, text="Jet Distance", command=self.c_ssort)
        self.b_ssort.pack(fill=X)
        #self.b_ssort.config(state=DISABLED)
        
        self.b_zsort = Button(self.botleftframe, text="Magie", command=self.c_zsort)
        self.b_zsort.pack(fill=X)
        #self.b_zsort.config(state=DISABLED)
        
        self.b_bsort = Button(self.botleftframe, text="Soin", command=self.c_bsort)
        self.b_bsort.pack(fill=X)
        #self.b_bsort.config(state=DISABLED)
        
        # Terrible hack to overcome limitation of OptionMenu...
        class MyIntVar(IntVar):
            def __init__(self, master, demo):
                self.demo = demo
                IntVar.__init__(self, master)
            def set(self, value):
                IntVar.set(self, value)
                if str(value) != '0':
                    self.demo.resize(value)

        #self.v_size = MyIntVar(self.master, self)
        #self.v_size.set(size)
        #sizes = [1, 2, 3, 4] + list(range(5, 55, 5)) #génère une liste entre 5 et 55 step 5
        #if self.size not in sizes:
            #sizes.append(self.size)
            #sizes.sort()
        #self.m_size = OptionMenu(self.botleftframe, self.v_size, *sizes)
        #self.m_size.pack(fill=X)

        self.v_speed = StringVar(self.master)
        self.v_speed.set("Pouvoirs")
        self.m_speed = OptionMenu(self.botleftframe, self.v_speed, "Recup", "Remede", "Barriere", "Mirroir", "Ralenti", "Accélère", "Revive", "Feu", "Glace", "Tonder", "Rayon")
        self.m_speed.pack(fill=X)
        #self.m_speed.config(state=DISABLED)

        self.v_speed = StringVar(self.master)
        self.v_speed.set("Écoles Magie")
        self.m_speed = OptionMenu(self.botleftframe, self.v_speed, "Sorts", "Runes", "Disciplines", "Techniques", "Elemental") #bouton détoulant
        self.m_speed.pack(fill=X)
        #self.m_speed.config(state=DISABLED)
        
        self.b_stepi = Button(self.botrightframe, text="Chef", command=self.c_stepi)
        self.b_stepi.pack(fill=X)
        #self.b_stepi.config(state=DISABLED)
        
        self.b_randomize = Button(self.botrightframe, text="Barbar", command=self.c_randomize)
        self.b_randomize.pack(fill=X)
        #self.b_randomize.config(state=DISABLED)
        
        self.b_uniform = Button(self.botrightframe, text="Archer", command=self.c_uniform)
        self.b_uniform.pack(fill=X)
        #self.b_uniform.config(state=DISABLED)
        
        self.b_distinct = Button(self.botrightframe, text="Black-Mage", command=self.c_distinct)
        self.b_distinct.pack(fill=X)
        #self.b_distinct.config(state=DISABLED)
        
        self.b_demo = Button(self.botrightframe, text="Guerrisseur", command=self.c_demo)
        self.b_demo.pack(fill=X)
        #self.b_demo.config(state=DISABLED)
        
        self.b_cancel = Button(self.botrightframe, text="Fuite", command=self.c_cancel)
        self.b_cancel.pack(fill=X)
        #self.b_cancel.config(state=ENABLED) #Acctivé

        self.b_quit = Button(self.botrightframe, text="Quitter", command=self.c_quit)
        self.b_quit.pack(fill=X)
        #self.b_quit.config(state=DISABLED)

    def resize(self, newsize):
        if self.busy:
            self.master.bell()
            return
        self.size = newsize
        self.array.setdata(range(1, self.size+1))

    def c_qsort(self):
        self.run(quicksort)

    def c_stepi(self):
        self.run(stepi)

    def c_isort(self):
        self.run(insertionsort)

    def c_ssort(self):
        self.run(selectionsort)

    def c_bsort(self):
        self.run(bubblesort)

    def c_zsort(self):
        self.run(magie)

    def c_demo(self):
        self.run(demosort)

    def c_randomize(self):
        self.run(randomize)

    def c_uniform(self):
        self.run(uniform)

    def c_distinct(self):
        self.run(distinct)

    def run(self, func):
        if self.busy:
            self.master.bell()
            return
        self.busy = 1
        self.array.setspeed(self.v_speed.get())
        self.b_cancel.config(state=NORMAL)
        try:
            func(self.array)
        except Array.Cancelled:
            pass
        self.b_cancel.config(state=DISABLED)
        self.busy = 0

    def c_cancel(self):
        if not self.busy:
            self.master.bell()
            return
        self.array.cancel()

    def c_step(self):
        if not self.busy:
            self.master.bell()
            return
        self.v_speed.set("Simple-étape")
        self.array.setspeed("Simple-étape")
        self.array.step()

    def c_quit(self):
        if self.busy:
            self.array.cancel()
        self.master.after_idle(self.master.quit)

def image():
    #Image
    import tkinter as Untitled
    fenetre = Untitled.Tk()
    photo = Untitled.PhotoImage(file='Untitled.png')
    label = Untitled.Label(fenetre, image=photo)
    label.pack()
    fenetre.mainloop()

def main():
    #Demo
    root = Tk()
    demo = SortDemo(root)#
    
    root.protocol('WM_DELETE_WINDOW', demo.c_quit)
    root.mainloop()
    
if __name__ == '__main__':
        main()
