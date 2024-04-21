from tkinter import *
import random

root = Tk()
root.title("Anaconda")
root.mainloop()

WIDTH = 800
HEIGHT = 600
SEG_SIZE = 20
IN_GAME = True

c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#ffffff")
c.grid()
c.focus_set()


# def create_block():
#     global BLOCK
#     posx = SEG_SIZE * random.randint(1, (WIDTH-SEG_SIZE) / SEG_SIZE)
#     posy = SEG_SIZE * random.randint(1, (WIDTH-SEG_SIZE) / SEG_SIZE)
#     BLOCK = c.create_oval(posx, posy, posx+SEG_SIZE, posy+SEG_SIZE, fill="red")
